from tkinter import messagebox
from re import *
import pyodbc 
from decouple import config
# Establshing connection with mssql
conn = pyodbc.connect(config('DB_CONNECTION'))
cursor = conn.cursor()


# Email entry validation function
def checkEmail(input_email_entry):
    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not search(regex_email,input_email_entry):   
            raise ValueError("Invalid Email!")

# Name entry validation function
def checkName(input_name_entry,name_entry):
    if not input_name_entry.isalpha():
        raise ValueError(name_entry+" should be alphabet only!")

# Password entry validation function
def checkPasswordLength(input_password_entry):
    if len(input_password_entry)<8:
        raise ValueError("Password length should be at least 8")

# Telephone number entry validation function
def checkTelephoneNumber(input_telephone_entry):
    regex_telephone='^01[0125][0-9]{8}$'
    if not search(regex_telephone,input_telephone_entry):   
            raise ValueError("Invalid Telephone Number!")

# Admin ID entry validation function
def checkAdminID(input_admin_id):
    if  not (input_admin_id.isnumeric() and input_admin_id[0:3]=="111" and len(input_admin_id)==7):   
            raise ValueError("Invalid Admin ID!")

# National ID entry validation function
def checkNationalID(input_national_id):
    if  not (input_national_id.isnumeric() and len(input_national_id)==14):   
            raise ValueError("Invalid National ID!")

# Grouped validations of client entries into one function
# (To shorten and improve the readability of [signUpClient])
def checkAllClientEntries(first_name,last_name,email,password,telephone):
    checkName(first_name,"First Name")
    checkName(last_name,"Last Name")
    checkEmail(email)
    checkPasswordLength(password)
    checkTelephoneNumber(telephone)
 
# Grouped validations of admin entries into one function
# (To shorten and improve the readability of [signUpAdmin])
def checkAllAdminEntries(admin_id,first_name,last_name,national_id,password,telephone):
    checkAdminID(admin_id)
    checkName(first_name,"First Name")
    checkName(last_name,"Last Name")
    checkNationalID(national_id)
    checkPasswordLength(password)
    checkTelephoneNumber(telephone)
    
# Format Altering Helper Functions  
def formatEmail(input_email_entry): 
    input_email_entry=input_email_entry.lower()
    return input_email_entry

def formatTelephone(input_telephone_entry): 
    if input_telephone_entry[0:2] == '+2':
        input_telephone_entry=input_telephone_entry[2:]
    return input_telephone_entry


#--------------------------------------------------Client--------------------------------------------------

# Accessing (inserting into) the database
# This function was created  to separate handle duplication/integrity exceptions throwed by pyodbc from [signUpClient]
# and to improve the readability of [signUpClient]
def insertClientIntoDB(first_name,last_name,email,password,telephone):
    try:
        cursor.execute(
            '''INSERT INTO CLIENT(FIRSTNAME,LASTNAME,EMAIL,[PASSWORD],TELEPHONENUM) 
               VALUES(?,?,?,?,?);''',first_name,last_name,email,password,telephone)
        conn.commit()
    except pyodbc.Error as ex:
        sqlstate= ex.args[0];
        if sqlstate == '23000':
            alreadyInUseValue=ex.args[1]
            indexOfValueDuplicated=alreadyInUseValue.find("is (")
            alreadyInUseValue=alreadyInUseValue[indexOfValueDuplicated+4:]
            endOfValueIndex=alreadyInUseValue.find(")")
            alreadyInUseValue=alreadyInUseValue[:endOfValueIndex]   
            raise ValueError(alreadyInUseValue+" is already in use")
        
#The main function that is be called by the gui component ~ button      
def signUpClient(first_name_entry,last_name_entry,email_entry,password_entry,telephone_entry):
    first_name=first_name_entry.get()
    last_name=last_name_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    telephone=telephone_entry.get()
    if not(first_name.strip() and last_name.strip() and email.strip() and password.strip() and telephone.strip()):
        messagebox.showerror("Sign Up failed","All fields are required!")
    else:
        try:
            email=formatEmail(email)
            telephone=formatTelephone(telephone)
            checkAllClientEntries(first_name,last_name,email,password,telephone)
            insertClientIntoDB(first_name,last_name,email,password,telephone)
            messagebox.showinfo("Success","Signed Up Successfully, Welcome "+first_name+" "+last_name)
            print("Log: ",first_name," ",last_name," ",email," ",password," ",telephone)
        except ValueError as error_message:
            messagebox.showerror("Sign Up failed",error_message)


#--------------------------------------------------Admin--------------------------------------------------

# Accessing (inserting into) the database
# This function was created  to separate handle duplication/integrity exceptions throwed by pyodbc from [signUpAdmin]
# and to improve the readability of [signUpAdmin]            
def insertAdminIntoDB(admin_id,first_name,last_name,national_id,password,telephone):
    try:
        cursor.execute(
            '''INSERT INTO ADMIN(ADMINID,FIRSTNAME,LASTNAME,NATIONALID,[PASSWORD],TELEPHONENUM) 
               VALUES(?,?,?,?,?,?);''',admin_id,first_name,last_name,national_id,password,telephone)
        conn.commit()
    except pyodbc.Error as ex:
        sqlstate= ex.args[0];
        if sqlstate == '23000':
            alreadyInUseValue=ex.args[1]
            indexOfValueDuplicated=alreadyInUseValue.find("is (")
            alreadyInUseValue=alreadyInUseValue[indexOfValueDuplicated+4:]
            endOfValueIndex=alreadyInUseValue.find(")")
            alreadyInUseValue=alreadyInUseValue[:endOfValueIndex]   
            raise ValueError(alreadyInUseValue+" is already in use")
        
#The main function that is be called by the gui component ~ button           
def signUpAdmin(admin_id_entry,first_name_entry,last_name_entry,national_id_entry,password_entry,telephone_entry):
    admin_id=admin_id_entry.get()
    first_name=first_name_entry.get()
    last_name=last_name_entry.get()
    national_id=national_id_entry.get()
    password=password_entry.get()
    telephone=telephone_entry.get()
    if not(admin_id.strip() and first_name.strip() and last_name.strip() and national_id.strip() and password.strip() and telephone.strip()):
        messagebox.showerror("Sign Up failed","All fields are required!")
    else:
        try:
            telephone=formatTelephone(telephone)
            checkAllAdminEntries(admin_id,first_name,last_name,national_id,password,telephone)
            insertAdminIntoDB(admin_id,first_name,last_name,national_id,password,telephone)
            messagebox.showinfo("Success","Signed Up Successfully, Welcome Admin "+first_name+" "+last_name)
            print("Log: ",admin_id," ",first_name," ",last_name," ",national_id," ",password," ",telephone)
        except ValueError as error_message:
            messagebox.showerror("Sign Up failed",error_message)
