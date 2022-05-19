from tkinter import messagebox
from re import *

def checkEmail(input_email_entry):
    input_email_entry=input_email_entry.lower()
    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not search(regex_email,input_email_entry):   
            raise ValueError("Invalid Email!")

def checkName(input_name_entry,name_entry):
    if not input_name_entry.isalpha():
        raise ValueError(name_entry+" should be alphabet only!")
def checkPasswordLength(input_password_entry):
    if len(input_password_entry)<8:
        raise ValueError("Password length should be at least 8")
def checkTelephoneNumber(input_telephone_entry):
    regex_telephone='^01[0125][0-9]{8}$'

    if input_telephone_entry[0:2] == '+2':
        input_telephone_entry=input_telephone_entry[2:]

    if not search(regex_telephone,input_telephone_entry):   
            raise ValueError("Invalid Telephone Number!")
def checkAll(first_name,last_name,email,password,telephone):
    checkName(first_name,"First Name")
    checkName(last_name,"Last Name")
    checkEmail(email)
    checkPasswordLength(password)
    checkTelephoneNumber(telephone)
    messagebox.showinfo("Success","Signed Up Successfully, Welcome "+first_name+" "+last_name)
    print("Log: ",first_name," ",last_name," ",email," ",password," ",telephone)

def signUp(first_name_entry,last_name_entry,email_entry,password_entry,telephone_entry):
    first_name=first_name_entry.get()
    last_name=last_name_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    telephone=telephone_entry.get()
    if not(first_name.strip() and last_name.strip() and email.strip() and password.strip() and telephone.strip()):
        messagebox.showerror("Sign Up failed","All fields are required!")
    else:
        try:
            checkAll(first_name,last_name,email,password,telephone)
        except ValueError as error_message:
            messagebox.showerror("Sign Up failed",error_message)
