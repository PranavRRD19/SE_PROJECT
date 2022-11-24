from library import *
from admin_home import admin_home

def admin_add_employee():
    
    #Clears screen
    os.system("cls")
    
    count=0
    #print(chalk.yellow.bold(figlet_format("ADMIN ADD", font="standard")))
    print(chalk.green.bold.underline("--------------ADMIN ADD EMPLOYEE--------------"))
    
    #Taking number of employees to add
    n=int(input("\nEnter the number of employees you want to add : "))
    for i in range(n):
        #Connecting to database
        mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
        mycursor = mydb.cursor()
        
        #Employee id as an input
        empid=input("\nEnter the employee id : ")
        
        #Checking if user has already been added
        mycursor.execute("SELECT * FROM empid_list where emp_id=%s",(empid,))
        
        #If user already added, display the error message 
        myresult = mycursor.fetchone()
        if myresult!=None:
            print("An employee with this employee id already exists")
            
        #If user not added, add employee Id to the database
        elif myresult==None:
            count+=1
            mycursor.execute("insert into empid_list values (%s)",(empid,))
            mydb.commit()
    print(chalk.blue.bold.underline(count),chalk.blue.bold.underline("\nEmployee(s) added"))
    input("Press Enter to continue")
    admin_home()
