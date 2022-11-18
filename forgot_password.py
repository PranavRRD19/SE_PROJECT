from library import *
from main1 import landing_page
from progress_bar import *


def user_forgot_helper():
    os.system("cls")
    print(chalk.red.bold.underline(
            "\n\t------------------------------ FORGOT PASSWORD------------------------------\n"))
    emp_id = inquirer.text(message="Enter your EMP_ID")
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM user_details where emp_id=%s", (emp_id,))
    myresult = mycursor.fetchone()
    if myresult!=None:
        user_forgot_password(myresult[0])
    else:
        print("The entered username/empid does not exist\n")
        questions = [
                        inquirer.List('value',
                        message='Do you want to try logging in again?',
                        choices=['Yes','No'],
                        ),
                ]
        answer = inquirer.prompt(questions)['value']
        if(answer=="Yes"):
                user_forgot_helper()
        elif(answer=="No"):
            landing_page()


def user_forgot_password(username):
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT security_question FROM user_details where emp_id=%s", (username,))
    myresult = mycursor.fetchone()
    print("\nThe security question you had set was: ",myresult[0])
    print("\n")
    security_answer = inquirer.text(message="Enter answer for your security question")
    mycursor.execute(
        "SELECT name,emp_id,security_answer FROM user_details where emp_id=%s AND security_answer=%s", (username,security_answer))
    result = mycursor.fetchone()
    # print("\n")
    if(result!=None):
        print("Requesting to Change password")
        text="Verifying_Data"
        progress_bar(text)
        print("\n", end="\n")
        print("DATA SUCCESSFULLY VERIFIED\n")
        new_password = input("Enter your new password : ")
        mycursor.execute(
        "UPDATE user_details SET password=%s where emp_id=%s AND security_answer=%s", (new_password,username,security_answer))
        text_ = "Updating Password"
        progress_bar(text_)
        print("\n", end="\n")
        print("PASSWORD SUCCESFULLY CHANGED AND UPDATED IN DATABASE\n")
        mydb.commit()
        input("\nPress enter to continue...")
        landing_page()

    elif(result==None):
        print("The credentials you have entered is incorrect.Try again")
        questions = [
                        inquirer.List('value',
                        message='\nDo you want to try logging in again?',
                        choices=['Yes','No'],
                        ),
                ]
        answer = inquirer.prompt(questions)['value']
        if(answer=="Yes"):
                user_forgot_helper()
        elif(answer=="No"):
            landing_page()