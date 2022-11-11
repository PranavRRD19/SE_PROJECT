import inquirer
import requests
import sys
from simple_chalk import chalk
from pyfiglet import figlet_format
import os
from tabulate import tabulate
import mysql.connector
import time

def landing_page():
    os.system("cls")
    print(chalk.yellow.bold(figlet_format("Helping Hands", font="standard")))
    questions = [
                        inquirer.List('value',
                        message='Enter your choice',
                        choices=['User Login', 'User Signup', 'About Us','Exit'],
                        ),
                ]
    answer = inquirer.prompt(questions)['value']
    if(answer=="User Login"):
        login()
    elif(answer=="User Signup"):
        signup()
    elif(answer=='About Us'):
        aboutus()
    else:
        exit()

def login():
    """ Display welcome message followed by a login prompt. """
    os.system("cls")
    print(chalk.blue.bold(figlet_format("LOGIN PAGE", font="standard"))) # welcome message
    username = inquirer.text(message="Enter your Username")
    password = inquirer.password(message="Enter your Password")
    #print(pin)
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM admin where username=%s and password=%s",(username, password))
    myresult = mycursor.fetchone()
    if myresult!=None:
        admin_home()
    elif myresult==None:
        print("check user")

def signup():
    os.system("cls")
    print("cooming up on sunday")

def aboutus():
    os.system("cls")
    print("abbu bucker shd write")

def admin_home():
    os.system("cls")
    print(chalk.blue.bold(figlet_format("Hi Admin", font="standard")))
    questions = [
                        inquirer.List('value',
                        message='Enter your choice',
                        choices=['Add Employee', 'View job vacancies', 'Add branch','Add Department','Update jobs'],
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
    

def admin_add_employee():
    #logic here
    os.system("cls")
    count=0
    #print(chalk.yellow.bold(figlet_format("ADMIN ADD", font="standard")))
    print(chalk.green.bold.underline("--------------ADMIN ADD EMPLOYEE--------------"))
    n=int(input("\nEnter the number of employees you want to add : "))
    for i in range(n):
        mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands")
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
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands")
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
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands")
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
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands")
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
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands")
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