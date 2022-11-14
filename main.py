import os
import sys
import time

import inquirer
import mysql.connector
import requests
from pyfiglet import figlet_format
from simple_chalk import chalk
from tabulate import tabulate
from termcolor import colored


def landing_page():
    os.system("cls")
    print(chalk.yellow.bold(figlet_format("Helping Hands", font="standard")))
    questions = [
        inquirer.List('value',
                      message='Enter your choice',
                      choices=['User Login', 'User Signup',
                               'About Us', 'Change Dept/Branch', 'Exit'],
                      ),
    ]
    answer = inquirer.prompt(questions)['value']
    if (answer == "User Login"):
        login()
    elif (answer == "User Signup"):
        signup()
    elif (answer == 'About Us'):
        aboutus()
    elif (answer == "Change Dept/Branch"):
        user_dept_branch_change()
    else:
        exit()


def login():
    """ Display welcome message followed by a login prompt. """
    os.system("cls")
    # welcome message
    print(chalk.blue.bold(figlet_format("LOGIN PAGE", font="standard")))
    username = inquirer.text(message="Enter your Username")
    password = inquirer.password(message="Enter your Password")
    # print(pin)
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands")
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM admin where username=%s and password=%s", (username, password))
    myresult = mycursor.fetchone()
    if myresult != None:
        admin_home()
    elif myresult == None:
        print("check user")
        mycursor.execute(
            "SELECT emp_id, name, phone_number, date_of_birth, gender, branch_id, dept_id FROM user_details where emp_id=%s and password=%s", (username, password))
        myresult = mycursor.fetchone()
        if myresult != None:
            # call user_pagehome here with uname n pw as parameters. The below code add it to user_view_profile
            # l = []
            # for values in myresult:
            #    l.append(values)
            # attr = ['emp_id', 'name', 'phone_number',
            #         'date_of_birth', 'gender', 'branch_id', 'dept_id']
            # print(tabulate(l, headers=attr, tablefmt="fancy_grid"))
            # print(l[3])
            # input("Press Enter to logout")
            # landing_page()
            l = []
            for values in myresult:
                l.append(values)
            attr = ['emp_id', 'name', 'phone_number',
                    'date_of_birth', 'gender', 'branch_id', 'dept_id']
            print(tabulate(l, headers=attr, tablefmt="fancy_grid"))
            input("Press Enter to logout")
            landing_page()
        elif myresult == None:
            print(chalk.blue.bold.underline(
                "\nEmployee doesn't exist / not registered"))
            input("Press Enter to continue")
            landing_page()


def signup():
    os.system("cls")
    #print("cooming up on sunday")
    print(chalk.blue.bold(figlet_format("SIGN IN PAGE", font="standard")))
    username = inquirer.text(message="Enter your Username/EMPID")
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands")
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM empid_list where emp_id=%s", (username,))
    myresult = mycursor.fetchone()
    if myresult == None:
        print(chalk.blue.bold.underline("\nEmployee doesn't exist"))
        input("Press Enter to continue")
        landing_page()
    mycursor.execute(
        "SELECT * FROM user_details where emp_id=%s", (username,))
    myresult = mycursor.fetchone()
    if myresult != None:
        print(chalk.blue.bold.underline("\nUsername already registered"))
        input("Press Enter to continue")
        landing_page()
    else:
        name = input("Name: ")
        dob = input("Date of Birth(format)")
        phone_number = input("Phone number")
        id = input("empid/username")
        password = input("Password")
        gender = input("Gender")
        curr_branch = input("Current branch id id you are working for")
        curr_dept = input("Current department id you are working for")
        mycursor.execute("INSERT INTO user_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                         (id, name, phone_number, dob, password, gender, curr_branch, curr_dept))
        mydb.commit()
        print(chalk.blue.bold.underline("\nUsername successfully registered"))
        input("Press Enter to continue")
        landing_page()


def aboutus():
    os.system("cls")
    print(chalk.red.bold(figlet_format("About Us", font="standard")))
    ENIGMA = colored("ENIGMA", "green", "on_grey")
    print(f"-> Helping Hands is a distributed software developed to maintain the details of employees working in any organization.\n\n-> This was built by Team {ENIGMA} under the guidance of Anand sir.\n\n-> This software has been developed to override the problems prevailing in the practicing manual system.\n\n-> Developed a well designed database to store the information.\n\n-> It aims to help both admin and employees of  a particular organization.\n\n-> The admin can perform various operations such as adding a department,deleting a department etc.\n\n-> It also helps employee to choose their preferred branch and department.\n\n-> We have built a very user friendly application that requires minimal training.")


def admin_home():
    os.system("cls")
    print(chalk.blue.bold(figlet_format("Hi Admin", font="standard")))
    questions = [
        inquirer.List('value',
                      message='Enter your choice',
                      choices=['Add Employee', 'View job vacancies',
                               'Add branch', 'Add Department', 'Update jobs', 'Logout'],
                      ),
    ]
    answer = inquirer.prompt(questions)['value']
    if (answer == "Add Employee"):
        admin_add_employee()
    elif (answer == "Add branch"):
        admin_add_branch()
    elif (answer == 'Add Department'):
        admin_add_department()
    elif (answer == 'View job vacancies'):
        view_jobs()
    elif (answer == 'Update jobs'):
        update_jobs()
    elif (answer == 'Logout'):
        landing_page()


def admin_add_employee():
    # logic here
    os.system("cls")
    count = 0
    #print(chalk.yellow.bold(figlet_format("ADMIN ADD", font="standard")))
    print(chalk.green.bold.underline(
        "--------------ADMIN ADD EMPLOYEE--------------"))
    n = int(input("\nEnter the number of employees you want to add : "))
    for i in range(n):
        mydb = mysql.connector.connect(
            host="localhost", user="root", database="helping_hands")
        mycursor = mydb.cursor()
        empid = input("\nEnter the employee id : ")
        mycursor.execute("SELECT * FROM empid_list where emp_id=%s", (empid,))
        myresult = mycursor.fetchone()
        if myresult != None:
            print("An employee with this employee id already exists")
        elif myresult == None:
            count += 1
            mycursor.execute("insert into empid_list values (%s)", (empid,))
            mydb.commit()
    print(chalk.blue.bold.underline(count),
          chalk.blue.bold.underline("\nEmployee(s) added"))
    input("Press Enter to continue")
    admin_home()


def admin_add_branch():
    # logic here
    os.system("cls")
    count = 0
    #print(chalk.yellow.bold(figlet_format("ADMIN ADD", font="standard")))
    print(chalk.green.bold.underline(
        "--------------ADMIN ADD BRANCH--------------"))
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands")
    mycursor = mydb.cursor()
    branch_name = input("Enter Branch name : ")
    branch_id = input("\nEnter the Branch id : ")
    branch_location = input("\nEnter the branch location : ")
    mycursor.execute("SELECT * FROM branch where branch_id=%s", (branch_id,))
    myresult = mycursor.fetchone()
    if myresult != None:
        print("\nA Branch with the given id already exists")
        questions = [
            inquirer.List('value',
                          message='\nDo you want to try adding a branch again?',
                          choices=['Yes', 'No'],
                          ),
        ]
        answer = inquirer.prompt(questions)['value']
        if (answer == "Yes"):
            admin_add_branch()
        elif (answer == "No"):
            admin_home()
    elif myresult == None:
        mycursor.execute("insert into branch values (%s, %s, %s)",
                         (branch_id, branch_name, branch_location))
        mydb.commit()
        print("\n")
        print(chalk.blue.bold.underline("Branch added ->"),
              chalk.blue.bold.underline(branch_id))
    print("\n")
    questions = [
        inquirer.List('value',
                      message='Do you want to add departments to this branch?',
                      choices=['Yes', 'No'],
                      ),
    ]
    answer = inquirer.prompt(questions)['value']
    if (answer == "Yes"):
        admin_add_department()
    elif (answer == "No"):
        admin_home()


def admin_add_department():
    os.system("cls")
    count = 0
    print(chalk.red.bold.underline(
        "--------------ADMIN ADD DEPARTMENT--------------"))
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands")
    mycursor = mydb.cursor()
    branch_id = input("\nEnter the Branch id : ")
    mycursor.execute("SELECT * FROM branch where branch_id=%s", (branch_id,))
    myresult = mycursor.fetchone()
    if myresult == None:
        print("\nA Branch id entered does not exist")
        print("\n")
        questions = [
            inquirer.List('value',
                          message='Do you want to try adding departments for a different branch id?',
                          choices=['Yes', 'No'],
                          ),
        ]
        answer = inquirer.prompt(questions)['value']
        if (answer == "Yes"):
            admin_add_department()
        elif (answer == "No"):
            admin_home()
    elif myresult != None:
        n = int(input("\nEnter the number of departments for branch :"))
        for i in range(n):
            dept_name = input("\nEnter the department name :")
            dept_id = input("\nEnter the department id for the branch : ")
            total_jobs = int(input("\nEnter the total number of jobs : "))
            vacant_jobs = int(
                input("\nEnter the total number of vacant jobs : "))
            mycursor.execute(
                "select * from department where dept_id = %s", (dept_id,))
            myresult = mycursor.fetchone()
            if myresult != None:
                print(
                    "\nThis department id already exists. This will not be added to the database")
            elif myresult == None:
                count += 1
                mycursor.execute("insert into department values (%s, %s, %s, %s, %s)",
                                 (branch_id, dept_id, dept_name, total_jobs, vacant_jobs))
                mydb.commit()
                print("\n")
                print(chalk.blue.bold.underline("Department added ->"),
                      chalk.blue.bold.underline(dept_id))
        print("\n")
        print(chalk.blue.bold.underline(count),
              chalk.blue.bold.underline("Department(s) added"))
        input("\nPress Enter to continue")
        admin_home()


def helper_view_jobs():
    os.system("cls")
    print(chalk.red.bold.underline(
        "\n\t------------------------------VIEWING JOB VACANCIES------------------------------\n"))
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands")
    mycursor = mydb.cursor()
    l = list()
    mycursor.execute(
        "SELECT b.branch_name,b.branch_id, d.dept_name, d.dept_id, d.total_jobs, d.vacant_jobs FROM branch as b inner join department as d on b.branch_id = d.branch_id")
    myresult = mycursor.fetchall()
    for x in myresult:
        l.append(list(x))
    head = ["Branch name", "Branch id", "Deaprtment name",
            "Department id", "Total jobs", "Vacant jobs"]
    print(tabulate(l, headers=head, tablefmt="fancy_grid"))


def view_jobs():
    helper_view_jobs()
    input("\n\nPress Enter to continue")
    admin_home()


def update_jobs():
    helper_view_jobs()
    print("\n")
    print(chalk.blue.bold.underline(
        "\n---------------------------JOB UPDATION---------------------------\n"))
    print("Check the above table to update number of jobs\n")
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands")
    mycursor = mydb.cursor()
    branch_id = input("\nEnter the Branch id : ")
    dept_id = input("\nEnter the department id : ")
    mycursor.execute(
        "SELECT * FROM department where branch_id=%s and dept_id=%s", (branch_id, dept_id))
    myresult = mycursor.fetchone()
    if myresult == None:
        print("\nBranch/Department id entered does not exist")
        print("\n")
        questions = [
            inquirer.List('value',
                          message='Do you want to try updating again?',
                          choices=['Yes', 'No'],
                          ),
        ]
        answer = inquirer.prompt(questions)['value']
        if (answer == "Yes"):
            update_jobs()
        elif (answer == "No"):
            admin_home()
    elif myresult != None:
        print("\n")
        print("Here's the record : ")
        print("\n")
        l = []
        #mycursor.execute("SELECT * from department where branch_id=%s and dept_id=%s",(branch_id,dept_id))
        mycursor.execute(
            "SELECT * from department where dept_id=%s", (dept_id,))
        myresult = mycursor.fetchall()
        for x in myresult:
            l.append(list(x))
        head = ["Branch id", "Department id",
                "Department name", "Total jobs", "Vacant jobs"]
        print(tabulate(l, headers=head, tablefmt="fancy_grid"))
        new_total_jobs = int(input("\nEnter the new total number of jobs : "))
        new_vacant_jobs = int(input("\nEnter the new vacant jobs : "))
        mycursor.execute("update department set total_jobs=%s, vacant_jobs=%s where branch_id=%s and dept_id=%s",
                         (new_total_jobs, new_vacant_jobs, branch_id, dept_id,))
        mydb.commit()
        print("\n")
        print("Number of jobs updated")
        input("Press Enter to continue...")
        admin_home()


def user_dept_branch_change():
    os.system("cls")
    print(chalk.blue.bold(figlet_format("CHANGE DEPT OR BRANCH", font="standard")))
    username = inquirer.text(message="Enter your Username/emp_id")
    password = inquirer.password(message="Enter your Password")
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands")
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT emp_id FROM user_details where emp_id=%s", (username,))
    myresult = mycursor.fetchone()
    if myresult != None:
        #########################################################
        def view_br_vac():
            os.system("cls")
            print(chalk.red.bold.underline(
            "\n\t------------------------------ JOB VACANCY AVAILABLE IN THESE BRANCHES------------------------------\n"))
            mydb = mysql.connector.connect(
            host="localhost", user="root", database="helping_hands")
            mycursor = mydb.cursor()
            l = list()
            mycursor.execute(
            "SELECT DISTINCT b.branch_name,b.branch_id FROM branch as b inner join department as d on b.branch_id = d.branch_id")
            myresult = mycursor.fetchall()
            for x in myresult:
                l.append(list(x))
            head = ["Branch name", "Branch id"]
            print(tabulate(l, headers=head, tablefmt="fancy_grid"))
        ################################################################
        def view_dep_vac(new_branch_id):
            #os.system("cls")
            print(chalk.red.bold.underline(
            "\n\t------------------------------ JOB VACANCY AVAILABLE IN SELECTED BRANCH------------------------------\n"))
            mydb = mysql.connector.connect(
            host="localhost", user="root", database="helping_hands")
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
            #return new_dept_id
        #####################################################################

        def vac_jobs(new_dept_id,new_branch_id,current_branch_id,current_dept_id):
            mycursor.execute(
                    "SELECT vacant_jobs FROM department WHERE branch_id = %s AND dept_id = %s", (new_branch_id, new_dept_id))
            new_result = mycursor.fetchone()
            c_a = int(new_result[0])
            minim = 1
            maxim = 0
            if (c_a < minim):
                print(
                    "We cannot allot you the selected branch and department since there is no vacany.\n")
                print(
                    "Either Choose different department in same branch or Choose different branch\n")
                print("Refer to the JOB VACANCIES TABLE displayed above")
                vac_jobs()
            elif (c_a > maxim):
                #n_b_i = int(new_branch_id[0])
                #n_d_i = int(new_dept_id[0])
                mycursor.execute("UPDATE user_details SET branch_id = %s, dept_id = %s WHERE emp_id = %s", (
                    new_branch_id, new_dept_id, username))
                mycursor.execute(
                    "SELECT vacant_jobs FROM department WHERE branch_id = %s AND dept_id = %s", (new_branch_id, new_dept_id))
                new_result = mycursor.fetchone()
                n_r = int(new_result[0])
                print("Congratulations!\n",
                      "Admin has changed your branch and department as requested\n")
                mycursor.execute("UPDATE department SET vacant_jobs = vacant_jobs-1 WHERE branch_id = %s AND dept_id=%s", (
                    new_branch_id, new_dept_id))
                print("CBI",current_branch_id)
                print("CDI",current_dept_id)
                print("NDI",new_dept_id)
                print("NBI",new_branch_id)
                mycursor.execute("UPDATE department SET vacant_jobs = vacant_jobs+1 WHERE branch_id = %s AND dept_id=%s", (
                    current_branch_id[0], current_dept_id[0]))
                mydb.commit()
                print("DB UPDATED!!!")
        #########################################################################
        
        view_br_vac()
        print("\n")
        newcursor = mydb.cursor()
        newcursor.execute(
            "SELECT branch_id FROM user_details where emp_id=%s", (username, ))
        current_branch_id = newcursor.fetchone()
        newcursor.execute(
            "SELECT dept_id FROM user_details where emp_id=%s", (username, ))
        current_dept_id = newcursor.fetchone()
        print("Current Branch your working in is:", current_branch_id)
        print("Current Department your working in is:", current_dept_id)
        #vac_jobs()
        new_branch_id = inquirer.text(
                message="Enter the branch_id you want to work in")
        view_dep_vac(new_branch_id)
        new_dept_id = inquirer.text(
            message="Enter the dept_id you want to work in")
        vac_jobs(new_dept_id,new_branch_id,current_branch_id,current_dept_id)

    elif (myresult == None):
        print("Employee doesnt exist.First get yourself registered")

if __name__ == "__main__":
    landing_page()
