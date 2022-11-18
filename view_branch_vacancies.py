from library import *

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
    