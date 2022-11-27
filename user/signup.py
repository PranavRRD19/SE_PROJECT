from library import *
from ..main1 import landing_page
from validation import *

def signup():
    os.system("cls")
    print(chalk.blue.bold(figlet_format("SIGN UP PAGE", font="standard")))
    username = inquirer.text(message="Enter your Username/EMPID")
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from empid_list where emp_id=%s", (username,))
    myresult = mycursor.fetchone()
    if myresult == None:
        print(chalk.blue.bold.underline("\nEmployee with the entered username is not a part of our company"))
        questions = [
                        inquirer.List('value',
                        message='\nDo you want to try signing up again?',
                        choices=['Yes','No'],
                        ),
                ]
        answer = inquirer.prompt(questions)['value']
        if(answer=="Yes"):
            signup()
        elif(answer=="No"):
            landing_page()
    elif myresult!=None:
        mycursor.execute("SELECT * FROM user_details where emp_id=%s", (username,))
        myresult = mycursor.fetchone()
        if myresult != None:
            print(chalk.blue.bold.underline("\nUsername already registered"))
            questions = [
                        inquirer.List('value',
                        message='Do you want to try signing up again?',
                        choices=['Yes','No'],
                        ),
                ]
            answer = inquirer.prompt(questions)['value']
            if(answer=="Yes"):
                signup()
            elif(answer=="No"):
                landing_page()
        else:
            questions=[
            inquirer.Text('name', message='Enter your name',validate=name_validation),
            #lunch
            inquirer.Text('dob',message='Enter your Date of Birth',validate=date_validation),
            inquirer.Text('phone_number', message='Enter your phone_number',validate=phone_validation),
            inquirer.Text('gender',message='Enter your Gender(M or F)',validate = gender_validation),
            inquirer.Text('security_question', message='Enter your security quesion. You may require this to change your password'),
            inquirer.Text('security_answer', message='Enter answer for the above question'),
            #validate in lunch
            inquirer.Text('curr_branch', message='Enter your current branch',validate=branch_validation),
            inquirer.Text('curr_dept', message='Enter your current department',validate=department_validation),
            ]
            answers = inquirer.prompt(questions)
            password=inquirer.password(message='Enter your password')
            mycursor.execute("INSERT INTO user_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (username, answers['name'], answers['phone_number'], answers['dob'], password, answers['gender'], answers['curr_branch'], answers['curr_dept'], answers['security_question'], answers['security_answer']))
            mydb.commit()
            # here, reduce number of vacant jobs by 1 for the entered branch and department
            print(chalk.blue.bold.underline("\nUsername successfully registered"))
            input("Press Enter to continue")
            landing_page()