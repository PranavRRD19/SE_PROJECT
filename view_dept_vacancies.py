from library import *

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