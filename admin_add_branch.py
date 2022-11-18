from library import *
from admin_home import admin_home
from admin_add_department import admin_add_department

def admin_add_branch():
    #logic here
    os.system("cls")
    count=0
    #print(chalk.yellow.bold(figlet_format("ADMIN ADD", font="standard")))
    print(chalk.green.bold.underline("--------------ADMIN ADD BRANCH--------------"))
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
    mycursor = mydb.cursor()
    branch_name=input("Enter Branch name : ")
    branch_id=input("\nEnter the Branch id : ")
    branch_location=input("\nEnter the branch location : ")
    mycursor.execute("SELECT * FROM branch where branch_id=%s",(branch_id,))
    myresult = mycursor.fetchone()
    if myresult!=None:
        print("\nA Branch with the given id already exists")
        questions = [
                        inquirer.List('value',
                        message='\nDo you want to try adding a branch again?',
                        choices=['Yes','No'],
                        ),
                ]
        answer = inquirer.prompt(questions)['value']
        if(answer=="Yes"):
            admin_add_branch()
        elif(answer=="No"):
            admin_home()
    elif myresult==None:
        mycursor.execute("insert into branch values (%s, %s, %s)",(branch_id,branch_name, branch_location))
        mydb.commit()
        print("\n")
        print(chalk.blue.bold.underline("Branch added ->"),chalk.blue.bold.underline(branch_id))
    print("\n")
    questions = [
                        inquirer.List('value',
                        message='Do you want to add departments to this branch?',
                        choices=['Yes','No'],
                        ),
                ]
    answer = inquirer.prompt(questions)['value']
    if(answer=="Yes"):
        admin_add_department()
    elif(answer=="No"):
        admin_home()