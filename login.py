from library import *
from admin_home import admin_home
from main1 import landing_page
from user_home import user_home

def login():
    """ Display welcome message followed by a login prompt. """
    os.system("cls")
    print(chalk.blue.bold(figlet_format("LOGIN PAGE", font="standard"))) # welcome message
    username = inquirer.text(message="Enter your Username")
    password = inquirer.password(message="Enter your Password")
    #print(pin)
    mydb = mysql.connector.connect(
        host="localhost",user="root",database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM admin where username=%s and password=%s",(username, password))
    myresult = mycursor.fetchone()
    if myresult!=None:
        admin_home()
    elif myresult==None:
        #print("check user")
        mycursor.execute(
            "SELECT * FROM user_details where emp_id=%s and password=%s", (username, password))
        myresult = mycursor.fetchone()
        #name=str(myresult[1])
        if myresult != None:
            name=str(myresult[1])
            user_home(username,name)
        elif myresult == None:
            print(chalk.blue.bold.underline(
                "\nWrong credentials"))
            questions = [
                        inquirer.List('value',
                        message='\nDo you want to try logging in again?',
                        choices=['Yes','No'],
                        ),
                ]
            answer = inquirer.prompt(questions)['value']
            if(answer=="Yes"):
                login()
            elif(answer=="No"):
                landing_page()