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

# Telephone number entry validation function
def checkTelephoneNumber(input_telephone_entry):
    regex_telephone='^01[0125][0-9]{8}$'
    if not search(regex_telephone,input_telephone_entry):   
            raise ValueError("Invalid Telephone Number!")

# National ID entry validation function
def checkNationalID(input_national_id):
    if  not (input_national_id.isnumeric() and len(input_national_id)==14):   
            raise ValueError("Invalid National ID!")

# def checkGender(gender_entry):
#     if not input_name_entry.isalpha():
#         raise ValueError(name_entry+" should be alphabet only!")

# def checklicenseDate(gender_entry):
#     if not input_name_entry.isalpha():
#         raise ValueError(name_entry+" should be alphabet only!")

def checkAllDriverData(first_name,last_name,telephone,gender,nationalID,licenseexpdate):
    checkName(first_name,"First Name")
    checkName(last_name,"Last Name")
    checkTelephoneNumber(telephone)
    # check
    checkNationalID(nationalID)
    # checklicenseDate(licenseexpdate)

# Format Altering Helper Functions  
def formatEmail(input_email_entry): 
    input_email_entry=input_email_entry.lower()
    return input_email_entry

def formatTelephone(input_telephone_entry): 
    if input_telephone_entry[0:2] == '+2':
        input_telephone_entry=input_telephone_entry[2:]
    return input_telephone_entry


def updateDriverInDB(first_name,last_name,telephone,gender,nationalID,licenseexpdate,driver_id_passed):
    try:
        cursor.execute("UPDATE DRIVER SET FIRSTNAME=?,LASTNAME=?,TELEPHONENUM=?,GENDER=?,NATIONALID=?, DRIVERLICENSEEXPIRYDATE=? WHERE DRIVERID = ?;",first_name,last_name,telephone,gender,nationalID,licenseexpdate,driver_id_passed)
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


def SaveDriver(firstname_entry,lastname_entry,phone_entry,gender_entry,nationalID_entry,licenseexpdate_entry,driver_id_passed):
    first_name=firstname_entry.get()
    last_name=lastname_entry.get()
    telephone=phone_entry.get()
    gender=gender_entry.get()
    nationalID=nationalID_entry.get()
    licenseexpdate=licenseexpdate_entry.get()

    if not(first_name.strip() and last_name.strip() and telephone.strip() and gender.strip() and nationalID.strip() and licenseexpdate.strip()):
        messagebox.showerror("Update failed","All fields are required!")
    else:
        try:
            telephone=formatTelephone(telephone)
            checkAllDriverData(first_name,last_name,telephone,gender,nationalID,licenseexpdate)
            updateDriverInDB(first_name,last_name,telephone,gender,nationalID,licenseexpdate,driver_id_passed)
            messagebox.showinfo("Success","Driver Data Updated Successfully")
        except ValueError as error_message:
            messagebox.showerror("Update failed",error_message)
