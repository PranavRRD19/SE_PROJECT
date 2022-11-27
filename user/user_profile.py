from library import *
from user_home import user_home

def user_profile(username, name):
    print(f"Profile of {name}")
    
    #Connecting to database
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
    mycursor = mydb.cursor()
    
    #Fetching details of the user (Using username as identifier to identify the row from the user_details table)
    mycursor.execute("SELECT emp_id, name, phone_number, date_of_birth, gender, branch_id, dept_id FROM user_details where emp_id=%s",(username,))
    myresult = mycursor.fetchone()
    branch_test=myresult[5]
    department_test=myresult[6]  
    l=[]
    #print(chalk.blue.bold(figlet_format(f"Hello {name}", font="standard")),)
    
    #Displaying the user details
    print(f"{'Employee Id:':<30}{myresult[0]:<40}")
    print(f"{'Name:':<30}{myresult[1]:<40}")
    print(f"{'Phone Number:':<30}{myresult[2]:<40}")
    print(f"{'Gender:':<30}{myresult[4]:<40}")
    print(f"{'Date of Birth(yyyy-mm-dd):':<30}{str(myresult[3]):<40}")
    if(branch_test==None):
        test="NULL"
        print(f"{'Branch Id:':<30}{test:<40}")
    else:
        print(f"{'Branch Id:':<30}{myresult[5]:<40}")

    if(department_test==None):
        test1="NULL"
        print(f"{'Department Id:':<30}{test1:<40}")  
    else:
        print(f"{'Department Id:':<30}{myresult[6]:<40}")  

    #On click enter event redirect to user_home
    input("\n\n\tPress Enter to go back.....")
    user_home(username, name)
