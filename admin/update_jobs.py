from library import *
from admin_home import admin_home
from view_jobs import *

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
