from library import *
from login import login
from signup import signup
from about_us import aboutus
from forgot_password import * 

def landing_page():
    os.system("cls")
    print(chalk.yellow.bold(figlet_format("Helping Hands for D Mart", font="standard")))
    questions = [
                        inquirer.List('value',
                        message='Enter your choice',
                        choices=['User Login', 'User Signup', 'About Us','Forgot Password','Exit'],
                        ),
                ]
    answer = inquirer.prompt(questions)['value']
    if(answer=="User Login"):
        login()
    elif(answer=="User Signup"):
        signup()
    elif(answer=='About Us'):
        aboutus()
    elif(answer=='Forgot Password'):
        user_forgot_helper()
    else:
        exit()


    
if __name__ == "__main__":
    landing_page()