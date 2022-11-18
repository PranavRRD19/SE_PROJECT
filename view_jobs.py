from library import *
from admin_home import admin_home

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