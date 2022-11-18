from library import *
from user_home import *

def vac_jobs(new_dept_id,new_branch_id,current_branch_id,current_dept_id, username):
    mydb = mysql.connector.connect(host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT vacant_jobs FROM department WHERE branch_id = %s AND dept_id = %s", (new_branch_id, new_dept_id))
    new_result = mycursor.fetchone()
    c_a = int(new_result[0])
    minim = 1
    maxim = 0
    if (c_a < minim):
        print("We cannot allot you the selected branch and department since there is no vacany.\n")
        print("Either Choose different department in same branch or Choose different branch\n")
        print("Refer to the JOB VACANCIES TABLE displayed above")
        vac_jobs()
    elif (c_a > maxim):
        mycursor.execute("UPDATE user_details SET branch_id = %s, dept_id = %s WHERE emp_id = %s", (new_branch_id, new_dept_id, username))
        mycursor.execute("SELECT vacant_jobs FROM department WHERE branch_id = %s AND dept_id = %s", (new_branch_id, new_dept_id))
        new_result = mycursor.fetchone()
        n_r = int(new_result[0])
        print("Congratulations!\n","Admin has changed your branch and department as requested\n")
        mycursor.execute("UPDATE department SET vacant_jobs = vacant_jobs-1 WHERE branch_id = %s AND dept_id=%s", (new_branch_id, new_dept_id))
        print("Your new Branch Id : ",new_branch_id)
        print("Your new Department Id : ",new_dept_id)
        mycursor.execute("UPDATE department SET vacant_jobs = vacant_jobs+1 WHERE branch_id = %s AND dept_id=%s", (current_branch_id[0], current_dept_id[0]))
        mydb.commit()
        mycursor.execute("select name from user_details where emp_id=%s", (username,))
        myresult = mycursor.fetchone()
        name= myresult[0]
        print("DB UPDATED!!!")
        input("Press Enter to continue")
        user_home(username, name)