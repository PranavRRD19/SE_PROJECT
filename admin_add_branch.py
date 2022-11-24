from library import *
from admin_home import admin_home
from admin_add_department import admin_add_department

def admin_add_branch():
    #clear screen
    os.system("cls")
    
    count=0
    print(chalk.green.bold.underline("--------------ADMIN ADD BRANCH--------------"))
    
    #connecting to database
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
    mycursor = mydb.cursor()
    
    #Taking inputs from admin to add a new Branch
    branch_name=input("Enter Branch name : ")
    branch_id=input("\nEnter the Branch id : ")
    branch_location=input("\nEnter the branch location : ")
    
    #Checking if Branch id is already in database
    mycursor.execute("SELECT * FROM branch where branch_id=%s",(branch_id,))
    myresult = mycursor.fetchone()
    
    #Throw an error message if branch id is already present in the database and ask user if he wants to try again
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
            
    #Else, add details to database and continue
    elif myresult==None:
        mycursor.execute("insert into branch values (%s, %s, %s)",(branch_id,branch_name, branch_location))
        mydb.commit()
        print("\n")
        print(chalk.blue.bold.underline("Branch added ->"),chalk.blue.bold.underline(branch_id))
    print("\n")
    
    #Asking user if he wants to add departments to this branch
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
