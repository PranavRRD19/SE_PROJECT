from library import *
from ..main1 import landing_page
from admin_add_employee import admin_add_employee
from admin_add_branch import admin_add_branch
from admin_add_department import admin_add_department
from view_jobs import view_jobs
from update_jobs import update_jobs
from admin_delete_branch import admin_delete_branch
from admin_delete_department import admin_delete_department
from admin_delete_employee import admin_delete_employee


def admin_home():
    
    #Clears screen
    os.system("cls")
    print(chalk.blue.bold(figlet_format("Hi Admin", font="standard")))
    
    #Provide admin with options to make a choice
    questions = [
                        inquirer.List('value',
                        message='Enter your choice',
                        choices=['Add Employee', 'View job vacancies', 'Add branch','Add Department','Update jobs','Delete Branch','Delete Department','View/Delete Employees','Logout'],
                        ),
                ]
    answer = inquirer.prompt(questions)['value']
    
    #Call functions based on admin choice
    if(answer=="Add Employee"):
        admin_add_employee()
    elif(answer=="Add branch"):
        admin_add_branch()
    elif(answer=='Add Department'):
        admin_add_department()
    elif(answer=='View job vacancies'):
        view_jobs()
    elif(answer=='Update jobs'):
        update_jobs()
    elif(answer=='Delete Branch'):
        admin_delete_branch()
    elif(answer=='Delete Department'):
        admin_delete_department()
    elif(answer=='View/Delete Employees'):
        admin_delete_employee()
    elif(answer=='Logout'):
        landing_page()
