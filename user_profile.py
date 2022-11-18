from library import *
from user_home import user_home

def user_profile(username, name):
    print(f"Profile of {name}")
    mydb = mysql.connector.connect(host="localhost",user="root",database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT emp_id, name, phone_number, date_of_birth, gender, branch_id, dept_id FROM user_details where emp_id=%s",(username,))
    myresult = mycursor.fetchone()  
    l=[]
    #print(chalk.blue.bold(figlet_format(f"Hello {name}", font="standard")),)
    print(f"{'Employee Id:':<30}{myresult[0]:<40}")
    print(f"{'Name:':<30}{myresult[1]:<40}")
    print(f"{'Phone Number:':<30}{myresult[2]:<40}")
    print(f"{'Gender:':<30}{myresult[4]:<40}")
    print(f"{'Date of Birth(yyyy-mm-dd):':<30}{str(myresult[3]):<40}")
    print(f"{'Branch Id:':<30}{myresult[5]:<40}")
    print(f"{'Department Id:':<30}{myresult[6]:<40}")   

    input("\n\n\tPress Enter to go back.....")
    user_home(username, name)