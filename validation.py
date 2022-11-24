from library import *

def phone_validation(answers, current):
	
	# If phone number doesn't consist of 10 numbers or if phone number doesn't start with either 6 0r 7 0r 8 or 9, return false as the phone number is invalid	
    if(len(current)!=10 or type(int(current))!=int or current[0] not in ['6','7','8','9']):
        return False
	#Else return true
    else:
        return True

def name_validation(answers, current):
	
	#If there exixts any digit in name field or if length of name(no of chars in name field) is 0, return false 
    flag = any(char.isdigit() for char in current)
    if(len(current)==0 or flag==True):
        print(len(current))
        return False
	#Else return true
    else:
        return True

def gender_validation(answers, current):
	
	#If the values entered in gender field is either M or m or F or f, return true
    if(current=='M' or current=='m' or current=='F' or current=='f'):
        return True
	#Else return false
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
	
	#Converting to string datatype
    current=str(current)

	#Connecting to database
    mydb = mysql.connector.connect(host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
	
	#Fetching branch details(using branch_id as identifer to identify thr row in branch table)
    mycursor.execute("SELECT * from branch where branch_id=%s", (current,))
    myresult = mycursor.fetchone()
	
	#If the branch_id doesn't exist in the branch table, return false
    if myresult == None:
        return False
	
	#Else return true
    else:
        return True

def department_validation(answers, current):
	
	#Converting to string datatype
    current=str(current)
	
	#connecting to database
    mydb = mysql.connector.connect(host="localhost", user="root", database="helping_hands1")
    mycursor = mydb.cursor()
	
	#Fetching department details(using dept_id as identifer to identify thr row in dept table)
    mycursor.execute("SELECT * from department where dept_id=%s", (current,))
    myresult = mycursor.fetchone()
	
	#If the dept_id doesn't exist in the dept table, return false
    if myresult == None:
        return False
	
	#Else return true
    else:
        return True
