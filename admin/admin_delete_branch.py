from library import *
from admin_home import *
from ..user.view_branch_vacancies import *

def admin_delete_branch():
    os.system("cls")
    print(chalk.blue.bold(figlet_format("DELETE BRANCH", font="standard")))
    
    #Connecting to database
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
        
    #Selecting the branch to be deleted
    questions = [
                inquirer.List('branch',
                message="Which Branch do you want to delete?",
                choices=l,
                ),
                ]
    answers = inquirer.prompt(questions)
    delete_branch_id=''.join(answers['branch'])
    
    #Deleting the selected branch
    mycursor.execute("delete from branch where branch_id=%s",(delete_branch_id,))
    mydb.commit()
    print("\n")
    
    #Displaying the selected branch
    print("Branch id : " + delete_branch_id + " " + "has been deleted")
    
     #On click enter event redirect to admin home page
    input("Press Enter to continue")
    admin_home()