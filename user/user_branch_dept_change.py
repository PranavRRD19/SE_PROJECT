from library import *
from view_branch_vacancies import view_br_vac
from view_dept_vacancies import view_dep_vac
from vacant_jobs import vac_jobs

def user_dept_branch_change(username):
    os.system("cls")
    print(chalk.blue.bold(figlet_format("CHANGE DEPT OR BRANCH", font="standard")))
    view_br_vac()
    print("\n")
    #newcursor = mydb.cursor()
    mydb = mysql.connector.connect(
            host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute(
            "SELECT branch_id FROM user_details where emp_id=%s", (username, ))
    current_branch_id = mycursor.fetchone()
    mycursor.execute(
            "SELECT dept_id FROM user_details where emp_id=%s", (username, ))
    current_dept_id = mycursor.fetchone()
    print("Current Branch ID you are working in is:", current_branch_id)
    print("Current Department ID you are working in is:", current_dept_id)

    l=list()
    #mycursor.execute("SELECT distinct branch_id from department where vacant_jobs>0")
    # myresult = mycursor.fetchone()
    # if myresult == None:
    #     mycursor.execute(
    #         "SELECT * FROM user_details where emp_id=%s", (username,))
    #     myresult = mycursor.fetchone()
    #     #name=str(myresult[1])
    #     if myresult != None:
    #         name=str(myresult[1])
    #     print("\nThere are no job vacancies in any of the branches")
    #     input("Press Enter to continue")
    #     user_home(username,name)
    #     #here
    #     mycursor.close()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT distinct branch_id from department where vacant_jobs>0")
    myresult = mycursor.fetchall()
    for x in myresult:
   	    l.append(list(x))
    questions = [
                inquirer.List('branch',
                message="What branch do you want",
                choices=l,
                ),
                ]
    answers = inquirer.prompt(questions)
    new_branch_id=''.join(answers['branch'])
    #new_branch_id = inquirer.text(message="Enter the branch_id you want to work in")
    view_dep_vac(new_branch_id)
    #new_dept_id = inquirer.text(message="Enter the dept_id you want to work in")
    mycursor.execute("SELECT dept_id from department where branch_id=%s and vacant_jobs>0",(new_branch_id,))
    l=list()
    myresult = mycursor.fetchall()
    for x in myresult:
   	    l.append(list(x))
    questions = [
                inquirer.List('dept',
                message="What dept do you want",
                choices=l,
                ),
                ]
    answers = inquirer.prompt(questions)
    new_dept_id=''.join(answers['dept'])
    vac_jobs(new_dept_id,new_branch_id,current_branch_id,current_dept_id, username)
