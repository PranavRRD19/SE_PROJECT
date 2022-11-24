from library import *
from main1 import landing_page
from user_profile import user_profile
from user_branch_dept_change import user_dept_branch_change

#User interface after logging in
def user_home(username, name):
    os.system("cls")
    username=username
    print(chalk.blue.bold(figlet_format(f"Hello {name}", font="standard")),)
    
    #Displaying the options to the user from which he can select
    questions = [
                        inquirer.List('value',
                        message='Enter your choice',
                        choices=['View profile', 'Change Branch/Department', 'Logout'],
                        ),
                ]
    answer = inquirer.prompt(questions)['value']
    
    #Directing to view profile
    if(answer=="View profile"):
        user_profile(username, name)
      
    #Directing to Change Branch/Department
    elif(answer=="Change Branch/Department"):
        user_dept_branch_change(username)
    
    #Logging out and redirecting to main page
    elif(answer=='Logout'):
        landing_page()
