# Importing mssql driver for connection
import pyodbc
from tkinter import messagebox

# Establshing connection with mssql
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Waddy;UID=-username-;PWD=-Password-')

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


# Function to retrieve input from textbox and attempt to login
def attemptLogIn(userId, password):
    enteredId = userId.get()
    enteredPass = password.get()

    if not(enteredId.strip() and enteredPass.strip()):
        messagebox.showerror("Log In failed","All fields are required!")
        return
    else:

        try:
            checkIdLength(enteredId)
            checkPasswordLength(enteredPass)

            isAdmin = True

            if enteredId.startswith("111"):
                cursor.execute("SELECT * from ADMIN where ADMINID = ? AND PASSWORD = ?", enteredId, enteredPass)
            else:
                isAdmin = False
                cursor.execute("SELECT * from CLIENT where CLIENTID = ? AND PASSWORD = ?", enteredId, enteredPass)

            userAccount = cursor.fetchone()

            if userAccount:
                messagebox.showinfo("Success","Logged In Successfully.")

                # Here a new page should open either the admin's or the client's main page
                #if isAdmin:
                    # code to link admin's main page
                #else:
                    # code to link client's main page
            else:
                messagebox.showinfo("Log In Failed","Invalid ID or password.")
                return

        except ValueError as error_message:
            messagebox.showerror("Log In failed",error_message)
