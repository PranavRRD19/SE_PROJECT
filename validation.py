from library import *

def phone_validation(answers, current):
    if(len(current)!=10 or type(int(current))!=int or current[0] not in ['6','7','8','9']):
        return False
    else:
        return True

def name_validation(answers, current):
    flag = any(char.isdigit() for char in current)
    if(len(current)==0 or flag==True):
        print(len(current))
        return False
    else:
        return True

def gender_validation(answers, current):
    if(current=='M' or current=='m' or current=='F' or current=='f'):
        return True
    else:
        return False

def date_validation(answers, current):
    format = "%Y-%m-%d"
    res = True
    try:
	    res = bool(datetime.strptime(str(current), format))
    except ValueError:
	    res = False
    return res

def branch_validation(answers, current):
    current=str(current)
    mydb = mysql.connector.connect(host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from branch where branch_id=%s", (current,))
    myresult = mycursor.fetchone()
    if myresult == None:
        return False
    else:
        return True

def department_validation(answers, current):
    current=str(current)
    mydb = mysql.connector.connect(host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from department where dept_id=%s", (current,))
    myresult = mycursor.fetchone()
    if myresult == None:
        return False
    else:
        return True