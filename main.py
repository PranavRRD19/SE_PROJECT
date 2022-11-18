import inquirer
import requests
import sys
from simple_chalk import chalk
from pyfiglet import figlet_format
import os
from tabulate import tabulate
import mysql.connector
import time
from termcolor import colored
from datetime import datetime

def landing_page():
    os.system("cls")
    print(chalk.yellow.bold(figlet_format("Helping Hands for D Mart", font="standard")))
    questions = [
                        inquirer.List('value',
                        message='Enter your choice',
                        choices=['User Login', 'User Signup', 'About Us','Forgot Password','Exit'],
                        ),
                ]
    answer = inquirer.prompt(questions)['value']
    if(answer=="User Login"):
        login()
    elif(answer=="User Signup"):
        signup()
    elif(answer=='About Us'):
        aboutus()
    elif(answer=='Forgot Password'):
        user_forgot_helper()
    else:
        exit()

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


def progress_bar(text):
    import time
    for j in range(1,101):
            time.sleep(.003)
     
            downloading = colored(text, 'green', 'on_grey', attrs=['reverse'])
            percentage = colored(f"[{j}%]", 'blue')
            bar = colored('|' * j, "red")
            color = downloading + percentage + bar
     
            print(color, end="\r")



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

def user_home(username, name):
    #get name from username
    os.system("cls")
    username=username
    print(chalk.blue.bold(figlet_format(f"Hello {name}", font="standard")),)
    questions = [
                        inquirer.List('value',
                        message='Enter your choice',
                        choices=['View profile', 'Change Branch/Department', 'Logout'],
                        ),
                ]
    answer = inquirer.prompt(questions)['value']
    if(answer=="View profile"):
        user_profile(username, name)
    elif(answer=="Change Branch/Department"):
        user_dept_branch_change(username)
    elif(answer=='Logout'):
        landing_page()

def user_profile(username, name):
    print(f"Profile of {name}")
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT emp_id, name, phone_number, date_of_birth, gender, branch_id, dept_id FROM user_details where emp_id=%s",(username,))
    myresult = mycursor.fetchone()  
    l=[]
    #print(chalk.blue.bold(figlet_format(f"Hello {name}", font="standard")),)
    print(f"{'Employee Id:':<30}{myresult[0]:<40}")
    print(f"{'Name:':<30}{myresult[1]:<40}")
    print(f"{'Phone Number:':<30}{myresult[2]:<40}")
    print(f"{'Gender:':<30}{myresult[4]:<40}")
    print(f"{'Date of Birth(yyyy-mm-dd):':<30}{str(myresult[3]):<40}")
    print(f"{'Branch Id:':<30}{myresult[5]:<40}")
    print(f"{'Department Id:':<30}{myresult[6]:<40}")   

    input("\n\n\tPress Enter to go back.....")
    user_home(username, name)

def view_br_vac():
    os.system("cls")
    print(chalk.red.bold.underline(
    "\n\t------------------------------ JOB VACANCY AVAILABLE IN THESE BRANCHES------------------------------\n"))
    mydb = mysql.connector.connect(
    host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    l = list()
    mycursor.execute("SELECT DISTINCT b.branch_name,b.branch_id FROM branch as b inner join department as d on b.branch_id = d.branch_id")
    myresult = mycursor.fetchall()
    for x in myresult:
        l.append(list(x))
    head = ["Branch name", "Branch id"]
    print(tabulate(l, headers=head, tablefmt="fancy_grid"))
    
def view_dep_vac(new_branch_id):
    #os.system("cls")
    print(chalk.red.bold.underline(
    "\n\t------------------------------ JOB VACANCY AVAILABLE IN SELECTED BRANCH------------------------------\n"))
    mydb = mysql.connector.connect(
    host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    l = list()
    mycursor.execute(
    "SELECT b.branch_name,b.branch_id, d.dept_name, d.dept_id, d.total_jobs, d.vacant_jobs FROM branch as b inner join department as d on b.branch_id = d.branch_id WHERE b.branch_id=%s AND d.vacant_jobs > 0",(new_branch_id,))
    myresult = mycursor.fetchall()
    for x in myresult:
        l.append(list(x))
    head = ["Branch name", "Branch id", "Deaprtment name",
    "Department id", "Total jobs", "Vacant jobs"]
    print(tabulate(l, headers=head, tablefmt="fancy_grid"))


def vac_jobs(new_dept_id,new_branch_id,current_branch_id,current_dept_id, username):
    mydb = mysql.connector.connect(host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT vacant_jobs FROM department WHERE branch_id = %s AND dept_id = %s", (new_branch_id, new_dept_id))
    new_result = mycursor.fetchone()
    c_a = int(new_result[0])
    minim = 1
    maxim = 0
    if (c_a < minim):
        print("We cannot allot you the selected branch and department since there is no vacany.\n")
        print("Either Choose different department in same branch or Choose different branch\n")
        print("Refer to the JOB VACANCIES TABLE displayed above")
        vac_jobs()
    elif (c_a > maxim):
        mycursor.execute("UPDATE user_details SET branch_id = %s, dept_id = %s WHERE emp_id = %s", (new_branch_id, new_dept_id, username))
        mycursor.execute("SELECT vacant_jobs FROM department WHERE branch_id = %s AND dept_id = %s", (new_branch_id, new_dept_id))
        new_result = mycursor.fetchone()
        n_r = int(new_result[0])
        print("Congratulations!\n","Admin has changed your branch and department as requested\n")
        mycursor.execute("UPDATE department SET vacant_jobs = vacant_jobs-1 WHERE branch_id = %s AND dept_id=%s", (new_branch_id, new_dept_id))
        print("Your new Branch Id : ",new_branch_id)
        print("Your new Department Id : ",new_dept_id)
        mycursor.execute("UPDATE department SET vacant_jobs = vacant_jobs+1 WHERE branch_id = %s AND dept_id=%s", (current_branch_id[0], current_dept_id[0]))
        mydb.commit()
        mycursor.execute("select name from user_details where emp_id=%s", (username,))
        myresult = mycursor.fetchone()
        name= myresult[0]
        print("DB UPDATED!!!")
        input("Press Enter to continue")
        user_home(username, name)

def user_dept_branch_change(username):
    os.system("cls")
    print(chalk.blue.bold(figlet_format("CHANGE DEPT OR BRANCH", font="standard")))
    view_br_vac()
    print("\n")
    #newcursor = mydb.cursor()
    mydb = mysql.connector.connect(
            host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute(
            "SELECT branch_id FROM user_details where emp_id=%s", (username, ))
    current_branch_id = mycursor.fetchone()
    mycursor.execute(
            "SELECT dept_id FROM user_details where emp_id=%s", (username, ))
    current_dept_id = mycursor.fetchone()
    print("Current Branch you are working in is:", current_branch_id)
    print("Current Department you are working in is:", current_dept_id)
    #vac_jobs()
    #below this 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
    l=list()
    mycursor.execute("SELECT distinct branch_id from department where vacant_jobs>0")
    myresult = mycursor.fetchall()
    for x in myresult:
   	    l.append(list(x))
    questions = [
                inquirer.List('branch',
                message="What branch do you want",
                choices=l,
                ),
                ]
    answers = inquirer.prompt(questions)
    new_branch_id=''.join(answers['branch'])
    #new_branch_id = inquirer.text(message="Enter the branch_id you want to work in")
    view_dep_vac(new_branch_id)
    #new_dept_id = inquirer.text(message="Enter the dept_id you want to work in")
    mycursor.execute("SELECT dept_id from department where branch_id=%s and vacant_jobs>0",(new_branch_id,))
    l=list()
    myresult = mycursor.fetchall()
    for x in myresult:
   	    l.append(list(x))
    questions = [
                inquirer.List('dept',
                message="What dept do you want",
                choices=l,
                ),
                ]
    answers = inquirer.prompt(questions)
    new_dept_id=''.join(answers['dept'])
    vac_jobs(new_dept_id,new_branch_id,current_branch_id,current_dept_id, username)


def phone_validation(answers, current):
    if(len(current)!=10 or type(int(current))!=int or current[0] not in ['6','7','8','9']):
        return False
    else:
        return True

def name_validation(answers, current):
    flag = any(char.isdigit() for char in current)
    if(len(current)==0 or flag==True):
        print(len(curr))
        return False
    else:
        return True

def gender_validation(answers, current):
    if(current=='M' or current=='m' or current=='F' or current=='f'):
        return True
    else:
        return False

def date_validation(answers, current):
    format = "%Y-%m-%d"
    res = True
    try:
	    res = bool(datetime.strptime(str(current), format))
    except ValueError:
	    res = False
    return res

def branch_validation(answers, current):
    current=str(current)
    mydb = mysql.connector.connect(host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from branch where branch_id=%s", (current,))
    myresult = mycursor.fetchone()
    if myresult == None:
        return False
    else:
        return True

def department_validation(answers, current):
    current=str(current)
    mydb = mysql.connector.connect(host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from department where dept_id=%s", (current,))
    myresult = mycursor.fetchone()
    if myresult == None:
        return False
    else:
        return True


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

def aboutus():
    os.system("cls")
    print(chalk.red.bold(figlet_format("About Us", font="standard")))
    ENIGMA = colored("ENIGMA", "green", "on_grey")
    #print("-> Helping Hands is a distributed software developed to maintain the details of employees working in any organization.\n-> This was built by Team", end=" ")
    print(f"-> Helping Hands is a distributed software developed to maintain the details of employees working in any organization.\n\n-> This was built by Team {ENIGMA} under the guidance of Anand sir.\n\n-> This software has been developed to override the problems prevailing in the practicing manual system.\n\n-> Developed a well designed database to store the information.\n\n-> It aims to help both admin and employees of  a particular organization.\n\n-> The admin can perform various operations such as adding a department,deleting a department etc.\n\n-> It also helps employee to choose their preferred branch and department.\n\n-> We have built a very user friendly application that requires minimal training.")
    input("\n\n\tPress Enter to go back.....")
    landing_page()

def admin_home():
    os.system("cls")
    print(chalk.blue.bold(figlet_format("Hi Admin", font="standard")))
    questions = [
                        inquirer.List('value',
                        message='Enter your choice',
                        choices=['Add Employee', 'View job vacancies', 'Add branch','Add Department','Update jobs','Logout'],
                        ),
                ]
    answer = inquirer.prompt(questions)['value']
    if(answer=="Add Employee"):
        admin_add_employee()
    elif(answer=="Add branch"):
        admin_add_branch()
    elif(answer=='Add Department'):
        admin_add_department()
    elif(answer=='View job vacancies'):
        view_jobs()
    elif(answer=='Update jobs'):
        update_jobs()
    elif(answer=='Logout'):
        landing_page()
    

def admin_add_employee():
    #logic here
    os.system("cls")
    count=0
    #print(chalk.yellow.bold(figlet_format("ADMIN ADD", font="standard")))
    print(chalk.green.bold.underline("--------------ADMIN ADD EMPLOYEE--------------"))
    n=int(input("\nEnter the number of employees you want to add : "))
    for i in range(n):
        mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
        mycursor = mydb.cursor()
        empid=input("\nEnter the employee id : ")
        mycursor.execute("SELECT * FROM empid_list where emp_id=%s",(empid,))
        myresult = mycursor.fetchone()
        if myresult!=None:
            print("An employee with this employee id already exists")
        elif myresult==None:
            count+=1
            mycursor.execute("insert into empid_list values (%s)",(empid,))
            mydb.commit()
    print(chalk.blue.bold.underline(count),chalk.blue.bold.underline("\nEmployee(s) added"))
    input("Press Enter to continue")
    admin_home()


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

def admin_add_department():
    os.system("cls")
    count=0
    print(chalk.red.bold.underline("--------------ADMIN ADD DEPARTMENT--------------"))
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
    mycursor = mydb.cursor()
    branch_id=input("\nEnter the Branch id : ")
    mycursor.execute("SELECT * FROM branch where branch_id=%s",(branch_id,))
    myresult = mycursor.fetchone()
    if myresult==None:
        print("\nA Branch id entered does not exist")
        print("\n")
        questions = [
                        inquirer.List('value',
                        message='Do you want to try adding departments for a different branch id?',
                        choices=['Yes','No'],
                        ),
                    ]
        answer = inquirer.prompt(questions)['value']
        if(answer=="Yes"):
            admin_add_department()
        elif(answer=="No"):
            admin_home()
    elif myresult!=None:
        n=int(input("\nEnter the number of departments for branch :"))
        for i in range(n):
            dept_name=input("\nEnter the department name :")
            dept_id=input("\nEnter the department id for the branch : ")
            total_jobs=int(input("\nEnter the total number of jobs : "))
            vacant_jobs=int(input("\nEnter the total number of vacant jobs : "))
            mycursor.execute("select * from department where dept_id = %s",(dept_id,))
            myresult = mycursor.fetchone()
            if myresult!=None:
                print("\nThis department id already exists. This will not be added to the database")
            elif myresult==None:
                count+=1
                mycursor.execute("insert into department values (%s, %s, %s, %s, %s)",(branch_id,dept_id, dept_name, total_jobs, vacant_jobs))
                mydb.commit()
                print("\n")
                print(chalk.blue.bold.underline("Department added ->"),chalk.blue.bold.underline(dept_id))
        print("\n")
        print(chalk.blue.bold.underline(count),chalk.blue.bold.underline("Department(s) added"))
        input("\nPress Enter to continue")
        admin_home()

def helper_view_jobs():
    os.system("cls")
    print(chalk.red.bold.underline("\n\t------------------------------VIEW JOB VACANCIES------------------------------\n"))
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
    mycursor = mydb.cursor()    
    l=list()
    mycursor.execute("SELECT b.branch_name,b.branch_id, d.dept_name, d.dept_id, d.total_jobs, d.vacant_jobs FROM branch as b inner join department as d on b.branch_id = d.branch_id")
    myresult = mycursor.fetchall()
    for x in myresult:
    	l.append(list(x))
    head = ["Branch name" , "Branch id" , "Deaprtment name" , "Department id" , "Total jobs", "Vacant jobs"]
    print(tabulate(l, headers=head, tablefmt="fancy_grid"))

def view_jobs():
    helper_view_jobs()
    input("\n\nPress Enter to continue")
    admin_home()

def update_jobs():
    helper_view_jobs()
    print("\n")
    print(chalk.blue.bold.underline("\n---------------------------JOB UPDATION---------------------------\n"))
    print("Check the above table to update number of jobs\n")
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
    mycursor = mydb.cursor()
    branch_id=input("\nEnter the Branch id : ")
    dept_id=input("\nEnter the department id : ")
    mycursor.execute("SELECT * FROM department where branch_id=%s and dept_id=%s",(branch_id,dept_id))
    myresult = mycursor.fetchone()
    if myresult==None:
        print("\nBranch/Department id entered does not exist")
        print("\n")
        questions = [
                        inquirer.List('value',
                        message='Do you want to try updating again?',
                        choices=['Yes','No'],
                        ),
                    ]
        answer = inquirer.prompt(questions)['value']
        if(answer=="Yes"):
            update_jobs()
        elif(answer=="No"):
            admin_home()
    elif myresult!=None:
        print("\n")
        print("Here's the record : ")
        print("\n")
        l=[]
        #mycursor.execute("SELECT * from department where branch_id=%s and dept_id=%s",(branch_id,dept_id))
        mycursor.execute("SELECT * from department where dept_id=%s",(dept_id,))
        myresult = mycursor.fetchall()
        for x in myresult:
    	    l.append(list(x))
        head = ["Branch id" , "Department id" , "Department name" , "Total jobs", "Vacant jobs"]
        print(tabulate(l, headers=head, tablefmt="fancy_grid"))
        new_total_jobs=int(input("\nEnter the new total number of jobs : "))
        new_vacant_jobs=int(input("\nEnter the new vacant jobs : "))
        mycursor.execute("update department set total_jobs=%s, vacant_jobs=%s where branch_id=%s and dept_id=%s",(new_total_jobs, new_vacant_jobs, branch_id, dept_id,))
        mydb.commit()
        print("\n")
        print("Number of jobs updated")
        input("Press Enter to continue...")
        admin_home()

    
if __name__ == "__main__":
    landing_page()