from tkinter import messagebox
from re import *
import pyodbc 
from decouple import config
from viewprofile import *
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

# Telephone number entry validation function
def checkTelephoneNumber(input_telephone_entry):
    regex_telephone='^01[0125][0-9]{8}$'
    if not search(regex_telephone,input_telephone_entry):   
            raise ValueError("Invalid Telephone Number!")

# National ID entry validation function
def checkNationalID(input_national_id):
    if  not (input_national_id.isnumeric() and len(input_national_id)==14):   
            raise ValueError("Invalid National ID!")

def checkGender(input_gender_entry):
    if not(input_gender_entry=="Male" or input_gender_entry=="Female"):
        raise ValueError("Not a valid input in gender field")

def checkAllClientData(first_name,last_name,email,telephone,gender):
    checkName(first_name,"First Name")
    checkName(last_name,"Last Name")
    checkTelephoneNumber(telephone)
    checkEmail(email)
    checkGender(gender)

def checkAllAdminData(first_name,last_name,nationalID,telephone,gender):
    checkName(first_name,"First Name")
    checkName(last_name,"Last Name")
    checkTelephoneNumber(telephone)
    checkNationalID(nationalID)
    checkGender(gender)

# Format Altering Helper Functions  
def formatEmail(input_email_entry): 
    input_email_entry=input_email_entry.lower()
    return input_email_entry

def formatTelephone(input_telephone_entry): 
    if input_telephone_entry[0:2] == '+2':
        input_telephone_entry=input_telephone_entry[2:]
    return input_telephone_entry

def formatGender(input_gender_entry):
    if(input_gender_entry=="male"):
        return "Male"
    if(input_gender_entry=="female"):
        return "Female"
    else:
        return input_gender_entry
    

#-----------------------------------------------------client-----------------------------------------------------------------------

def updateClientInDB(first_name,last_name,email,telephone,gender,client_id_passed,password):
    try:
        cursor.execute("UPDATE CLIENT SET FIRSTNAME=?,LASTNAME=?,EMAIL=?,PASSWORD=?,TELEPHONENUM=?,GENDER=? WHERE CLIENTID = ?;",first_name,last_name,email,password,telephone,gender,client_id_passed)
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


def SaveClient(firstname_entry,lastname_entry,email_entry,phone_entry,gender_entry,client_id_passed,password_entry):
    
    cursor=displayClientProfile(client_id_passed)
    clientData=cursor.fetchone()

    if not((phone_entry.get()).strip()):
        telephone = clientData[2]
    else:
        telephone = phone_entry.get()

    if not((firstname_entry.get()).strip()):
        first_name = clientData[0]
    else:
        first_name=firstname_entry.get()

    if not((lastname_entry.get()).strip()):
        last_name = clientData[1]
    else:
        last_name=lastname_entry.get()

    if not((email_entry.get()).strip()):
        email = clientData[4]
    else:
        email=email_entry.get()

    if not((password_entry.get()).strip()):
        password = clientData[5]
    else:
        password=password_entry.get()

    if (not((gender_entry.get()).strip())) or gender_entry.get() == " ":

        gender = clientData[3]
    else:
        gender=gender_entry.get()

    if not((phone_entry.get()).strip()):
        telephone = clientData[2]
    else:
        telephone=phone_entry.get()

 
    try:
        formattedGender = formatGender(gender)
        telephone=formatTelephone(telephone)
        checkAllClientData(first_name,last_name,email,telephone,formattedGender)
        updateClientInDB(first_name,last_name,email,telephone,formattedGender,client_id_passed,password)
        messagebox.showinfo("Success","Client Data Updated Successfully")
    except ValueError as error_message:
        messagebox.showerror("Update failed",error_message)

#-----------------------------------------------------Admin-----------------------------------------------------------------------

def updateAdminInDB(first_name,last_name,nationalID,telephone,gender,admin_id_passed,password):
    try:
        cursor.execute("UPDATE ADMIN SET FIRSTNAME=?,LASTNAME=?,NATIONALID=?,PASSWORD=?,TELEPHONENUM=?,GENDER=? WHERE ADMINID = ?;",first_name,last_name,nationalID,password,telephone,gender,admin_id_passed)
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


def SaveAdmin(firstname_entry,lastname_entry,nationalID_entry,phone_entry,gender_entry,admin_id_passed,password_entry):
    
    cursor=displayAdminProfile(admin_id_passed)
    adminData=cursor.fetchone()

    if not((phone_entry.get()).strip()):
        telephone = adminData[3]
    else:
        telephone = phone_entry.get()

    if not((firstname_entry.get()).strip()):
        first_name = adminData[0]
    else:
        first_name=firstname_entry.get()

    if not((lastname_entry.get()).strip()):
        last_name = adminData[1]
    else:
        last_name=lastname_entry.get()

    if not((nationalID_entry.get()).strip()):
        nationalID = adminData[2]
    else:
        nationalID = nationalID_entry.get()

    if not((password_entry.get()).strip()):
        password = adminData[5]
    else:
        password=password_entry.get()

    if (not((gender_entry.get()).strip())) or gender_entry.get() == " ":
        gender = adminData[4]
    else:
        gender=gender_entry.get()

    
    try:
        formattedGender = formatGender(gender)
        telephone=formatTelephone(telephone)
        checkAllAdminData(first_name,last_name,nationalID,telephone,formattedGender)
        updateAdminInDB(first_name,last_name,nationalID,telephone,formattedGender,admin_id_passed,password)
        messagebox.showinfo("Success","Admin Data Updated Successfully")
    except ValueError as error_message:
        messagebox.showerror("Update failed",error_message)
