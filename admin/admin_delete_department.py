from library import *
from admin_home import *
from ..user.view_branch_vacancies import *

def admin_delete_department():
    os.system("cls")
    print(chalk.blue.bold(figlet_format("DELETE DEPARTMENT", font="standard")))
    
    #connecting to database
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    
    #Calling branch vacancies function
    view_br_vac()
    mycursor.execute("SELECT branch_id from branch")
    myresult = mycursor.fetchall()
    l=list()
    for x in myresult:
   	    l.append(list(x))
    
    #selecting the branch from which the dept must be deleted
    questions = [
                inquirer.List('branch',
                message="Select the Branch from which you want to delete the Department",
                choices=l,
                ),
                ]
    answers = inquirer.prompt(questions)
    delete_branch_id=''.join(answers['branch'])
    
    #fetchting the dept id from the selected branch id 
    mycursor.execute("SELECT dept_id from department where branch_id=%s",(delete_branch_id,))
    myresult = mycursor.fetchall()
    l1=list()
    for x in myresult:
   	    l1.append(list(x))
    
    #seleting the dept id from the selected branch id to be deleted
    questions = [
                inquirer.List('dept',
                message="Which Department do you want to delete?",
                choices=l1,
                ),
                ]
    answers = inquirer.prompt(questions)
    delete_dept_id=''.join(answers['dept'])
    
    #deleting the selected dept id
    mycursor.execute("delete from department where branch_id=%s and dept_id=%s",(delete_branch_id,delete_dept_id))
    mydb.commit()
    print("\n")
    
    #displaying the deleted dept id and from also the branch id 
    print("Department id -> " + delete_dept_id + " from " + "Branch Id -> " + delete_branch_id + " has been deleted")
    
    #On click enter event redirect to admin home page
    input("Press Enter to continue")
    admin_home()