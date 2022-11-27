from library import *
from admin_home import *


def admin_delete_employee():
    os.system("cls")
    print(chalk.green.bold.underline("\n\n\t\t\t-----------------VIEW/DELETE EMPLOYEES-------------------\n\n"))
    
    #Connecting to database
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    l=list()
    
    #Fetching details of all employees
    mycursor.execute("SELECT emp_id,name,phone_number,date_of_birth,gender,branch_id,dept_id from user_details")
    myresult = mycursor.fetchall()
    for x in myresult:
    	l.append(list(x))
    
    head = ["Employee Id","Name","Phone Number","DOB","Gender","Branch Id","Department Id"]
    
    #displaying the details of all employees
    print(tabulate(l, headers=head, tablefmt="fancy_grid"))
    print("\n")
    
    #Option for admin to choose if he wants to delete any employee (yes to delete an employee, no to just view)
    questions = [
                        inquirer.List('value',
                        message='Do you want to delete an employee?',
                        choices=['Yes','No'],
                        ),
                ]
    answer = inquirer.prompt(questions)['value']
    
    #If selected no redirect to admin home
    if(answer=="No"):
        admin_home()  
    
    #else, displaying the emp_id and admin can choose the emp_id to delete  
    mycursor.execute("SELECT emp_id from user_details")
    myresult = mycursor.fetchall()
    l=[]
    for x in myresult:
   	    l.append(list(x))
    questions = [
                inquirer.List('emp_id',
                message="What employee do you want to delete?",
                choices=l,
                ),
                ]
    answers = inquirer.prompt(questions)
    delete_emp_id=''.join(answers['emp_id'])
    
    #Updating the details of job vacancies as no of job vacancies increases by 1 upon deleting
    mycursor.execute("update department as d inner join user_details as u on u.dept_id=d.dept_id and u.emp_id=%s set d.vacant_jobs=d.vacant_jobs+1",(delete_emp_id,))
    
    #deleting the employee from user_details table
    mycursor.execute("DELETE from user_details where emp_id=%s",(delete_emp_id,))
    
    # myresult = mycursor.fetchall()
    mydb.commit()
    
    print("\nAfter Deletion\n")
    l=list()
       
    #Fetching details of all employees after deleting
    mycursor.execute("SELECT emp_id,name,phone_number,date_of_birth,gender,branch_id,dept_id from user_details")
    myresult = mycursor.fetchall()
    for x in myresult:
    	l.append(list(x))
    head = ["Employee Id","Name","Phone Number","DOB","Gender","Branch Id","Department Id"]
    
    #Displaying details of all employees after deleting
    print(tabulate(l, headers=head, tablefmt="fancy_grid"))
    input("\nPress Enter to continue")
    admin_home()