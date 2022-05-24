from tkinter import messagebox
from re import *
import pyodbc 
from decouple import config
# Establshing connection with mssql
conn = pyodbc.connect(config('DB_CONNECTION'))
cursor = conn.cursor()

def displayClientProfile(client_id):
    cursor.execute('SELECT FirstName,LastName,TelephoneNum,Gender,Email from client where ClientID=?',client_id)
    return cursor 
