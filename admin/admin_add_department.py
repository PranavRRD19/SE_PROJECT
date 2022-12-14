from library import *
from admin_home import admin_home

def admin_add_department():
    #Cleards screen
    os.system("cls")
    
    count=0
    print(chalk.red.bold.underline("--------------ADMIN ADD DEPARTMENT--------------"))
    
    #Connecting to the database
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
    mycursor = mydb.cursor()
    
    #Taking Branch id to which department has to be added
    branch_id=input("\nEnter the Branch id : ")
    
    #Checking if Branch Id is present in the database
    mycursor.execute("SELECT * FROM branch where branch_id=%s",(branch_id,))
    myresult = mycursor.fetchone()
    
    #display an error message if branch id is not present and prompt the admin if he wants to enter a different branch id
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
            
    #If branch id is present in the database, take department details from admin
    elif myresult!=None:
        #Asking number of departments to add
        n=int(input("\nEnter the number of departments for branch :"))
        for i in range(n):
            dept_name=input("\nEnter the department name :")
            dept_id=input("\nEnter the department id for the branch : ")
            total_jobs=int(input("\nEnter the total number of jobs : "))
            vacant_jobs=int(input("\nEnter the total number of vacant jobs : "))
            
            #Checks if the department id is already present
            mycursor.execute("select * from department where dept_id = %s",(dept_id,))
            myresult = mycursor.fetchone()
            
            #Don't add to database if dept id is already there
            if myresult!=None:
                print("\nThis department id already exists. This will not be added to the database")
                
            #Add department details only if the department id is not already present
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
