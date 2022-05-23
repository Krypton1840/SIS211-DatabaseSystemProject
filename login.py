from tkinter import messagebox
from re import *
import pyodbc 
from decouple import config
# Establshing connection with mssql
conn = pyodbc.connect(config('DB_CONNECTION'))

# Creating a cursor to execute sql commands
cursor = conn.cursor()

# Function to check password length
def checkPasswordLength(input_password_entry):
    if len(input_password_entry) < 8:
        raise ValueError("Password length should be at least 8.")

# Function to check user id length
def checkIdLength(input_password_entry):
    if len(input_password_entry) != 7:
        raise ValueError("Id is 7 characters.")

# Format Altering Helper Functions  
def formatEmail(input_email_entry): 
    input_email_entry=input_email_entry.lower()
    return input_email_entry

#
def checkEmail(input_email_entry):
    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not search(regex_email,input_email_entry):   
            raise ValueError("Invalid Email!")

# Function to retrieve input from textbox and attempt to login as an admin
def attemptAdminLogIn(adminId, password):
    enteredId = adminId.get()
    enteredPass = password.get()

    if not(enteredId.strip() and enteredPass.strip()):
        messagebox.showerror("Log In failed","All fields are required!")
        return
    else:

        try:
            checkIdLength(enteredId)
            checkPasswordLength(enteredPass)

            if enteredId.startswith("111"):
                cursor.execute("SELECT * from ADMIN where ADMINID = ? AND PASSWORD = ?", enteredId, enteredPass)
            else:
                raise ValueError("The entered Admin ID is incorrect.")

            userAccount = cursor.fetchone()

            if userAccount:
                messagebox.showinfo("Success","Logged In Successfully.")

                # Here a new page should open the admin's main page
            else:
                messagebox.showerror("Log In Failed","Invalid ID or password.")
                return

        except ValueError as error_message:
            messagebox.showerror("Log In failed",error_message)

# Function to retrieve input from textbox and attempt to login as a client
def attemptClientLogIn(userEmail, password):
    enteredEmail = userEmail.get()
    enteredPass = password.get()

    if not(enteredEmail.strip() and enteredPass.strip()):
        messagebox.showerror("Log In failed","All fields are required!")
        return
    else:
        
        email = formatEmail(enteredEmail)
        try:
            checkEmail(email)
            checkPasswordLength(enteredPass)

            cursor.execute("SELECT * from CLIENT where EMAIL = ? AND PASSWORD = ?", enteredEmail, enteredPass)
            userAccount = cursor.fetchone()

            if userAccount:
                messagebox.showinfo("Success","Logged In Successfully.")

                # Here a new page should open the client's main page
            else:
                messagebox.showerror("Log In Failed","Invalid Email or password.")
                return

        except ValueError as error_message:
            messagebox.showerror("Log In failed",error_message)