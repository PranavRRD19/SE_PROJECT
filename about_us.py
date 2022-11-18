from library import *
from main1 import landing_page

def aboutus():
    os.system("cls")
    print(chalk.red.bold(figlet_format("About Us", font="standard")))
    ENIGMA = colored("ENIGMA", "green", "on_grey")
    #print("-> Helping Hands is a distributed software developed to maintain the details of employees working in any organization.\n-> This was built by Team", end=" ")
    print(f"-> Helping Hands is a distributed software developed to maintain the details of employees working in any organization.\n\n-> This was built by Team {ENIGMA} under the guidance of Anand sir.\n\n-> This software has been developed to override the problems prevailing in the practicing manual system.\n\n-> Developed a well designed database to store the information.\n\n-> It aims to help both admin and employees of  a particular organization.\n\n-> The admin can perform various operations such as adding a department,deleting a department etc.\n\n-> It also helps employee to choose their preferred branch and department.\n\n-> We have built a very user friendly application that requires minimal training.")
    input("\n\n\tPress Enter to go back.....")
    landing_page()
    