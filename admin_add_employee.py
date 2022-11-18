from library import *
from admin_home import admin_home

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