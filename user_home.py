from library import *
from main1 import landing_page
from user_profile import user_profile
from user_branch_dept_change import user_dept_branch_change

def user_home(username, name):
    #get name from username
    os.system("cls")
    username=username
    print(chalk.blue.bold(figlet_format(f"Hello {name}", font="standard")),)
    questions = [
                        inquirer.List('value',
                        message='Enter your choice',
                        choices=['View profile', 'Change Branch/Department', 'Logout'],
                        ),
                ]
    answer = inquirer.prompt(questions)['value']
    if(answer=="View profile"):
        user_profile(username, name)
    elif(answer=="Change Branch/Department"):
        user_dept_branch_change(username)
    elif(answer=='Logout'):
        landing_page()