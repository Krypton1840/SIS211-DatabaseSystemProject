import pyodbc 
from tkinter import messagebox
from re import *
import datetime
from decouple import config
# Establshing connection with mssql
conn = pyodbc.connect(config('DB_CONNECTION'))
cursor = conn.cursor()


def getTrips(tree):
           cursor.execute("SELECT COUNT(*) FROM trip")
           countOfTrips=cursor.fetchone()
           cursor.execute('SELECT TripID,FirstName,LastName,PickupTime,AvailableSeats,TripStatus,TripFee from trip inner join driver on trip.DriverID=driver.DriverID;')
           cell_colors=["cell1","cell2"]
           color_index=0
           tree.delete(*tree.get_children())
           for i in range(countOfTrips[0]):
                  tripData=cursor.fetchone()
                  if(tripData):
                    tree.insert('', 'end',text="1", values=(tripData[0],tripData[1]+" "+tripData[2],tripData[3],tripData[4],tripData[5],tripData[6]), tags=(cell_colors[color_index]))
                    if color_index==0:
                           color_index+=1
                    elif color_index==1:
                           color_index-=1;
def getDrivers(tree):
           cursor.execute("SELECT COUNT(*) FROM driver")
           countOfDrivers=cursor.fetchone()
           cursor.execute('SELECT driver.DRIVERID,commuterbus.COMMUTERBUSID,FIRSTNAME,LASTNAME,TELEPHONENUM,GENDER,NATIONALID,DRIVERLICENSEEXPIRYDATE,LICENSEPLATE,LICENSEEXPIRYDATE from driver inner join commuterbus on driver.DRIVERID=commuterbus.DRIVERID;')
           cell_colors=["cell1","cell2"]
           color_index=0
           tree.delete(*tree.get_children())
           for i in range(countOfDrivers[0]):
                  driverData=cursor.fetchone()
                  if(driverData):
                    tree.insert('', 'end',text="1", values=(driverData[0],driverData[1],driverData[2]+" "+driverData[3],driverData[4],driverData[5],driverData[6],driverData[7],driverData[8],driverData[9]), tags=(cell_colors[color_index]))
                    if color_index==0:
                           color_index+=1
                    elif color_index==1:
                           color_index-=1;

# Name entry validation function
def checkName(input_name_entry,name_entry):
    if not input_name_entry.isalpha():
        raise ValueError(name_entry+" should be alphabet only!")

def checkTelephoneNumber(input_telephone_entry):
    regex_telephone='^01[0125][0-9]{8}$'
    if not search(regex_telephone,input_telephone_entry):   
            raise ValueError("Invalid Telephone Number!")
    
# National ID entry validation function
def checkNationalID(input_national_id):
    if  not (input_national_id.isnumeric() and len(input_national_id)==14):   
            raise ValueError("Invalid National ID!")
        
# Gender entry validation function
def checkGender(input_gender_entry):
    if not(input_gender_entry=="Male" or input_gender_entry=="male" or input_gender_entry=="Female" or input_gender_entry=="female"):
        raise ValueError("Not a valid input in gender field")

def checkDate(date_entry):
    regex_date='^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$'
    if not search(regex_date,date_entry):
            raise ValueError("Invalid Date Entry")
    
def checkLicensePlate(license_plate_entry):
    if not (len(license_plate_entry)==7):
        raise ValueError("License plate should be of length 7")

# Format Altering Helper Functions  

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
  
  

def checkAllDriverEntries(first_name,last_name,telephone_number,gender,national_id,driver_license_expiry,license_plate,bus_license_expiry):
    checkName(first_name,"First Name")
    checkName(last_name,"Last Name")
    checkTelephoneNumber(telephone_number)
    checkNationalID(national_id)
    checkDate(driver_license_expiry)
    checkGender(gender)
    checkLicensePlate(license_plate)
    checkDate(bus_license_expiry)
  
  
  
    
def insertDriverIntoDB(first_name,last_name,telephone_number,gender,national_id,driver_license_expiry,license_plate,bus_license_expiry):
    try:
        cursor.execute(
            '''INSERT INTO DRIVER(FIRSTNAME,LASTNAME,TELEPHONENUM,GENDER,NATIONALID,DRIVERLICENSEEXPIRYDATE)
               VALUES(?,?,?,?,?,?);
               INSERT INTO COMMUTERBUS(DRIVERID,LICENSEPLATE,LICENSEEXPIRYDATE)
               VALUES(SCOPE_IDENTITY(),?,?)''',first_name,last_name,telephone_number,gender,national_id,driver_license_expiry,license_plate,bus_license_expiry)
        cursor.commit()
        
    except pyodbc.Error as ex:
        sqlstate= ex.args[0];
        if sqlstate == '23000':
            alreadyInUseValue=ex.args[1]
            indexOfValueDuplicated=alreadyInUseValue.find("is (")
            alreadyInUseValue=alreadyInUseValue[indexOfValueDuplicated+4:]
            endOfValueIndex=alreadyInUseValue.find(")")
            alreadyInUseValue=alreadyInUseValue[:endOfValueIndex]   
            raise ValueError(alreadyInUseValue+" is already in use")

    
                           
def addDriver(tree,first_name_entry,last_name_entry,telephone_number_entry,gender_entry,national_id_entry,driver_license_expiry_date_entry,license_plate_entry,bus_license_expiry_date_entry):
    first_name=first_name_entry.get()
    last_name=last_name_entry.get()
    telephone_number=telephone_number_entry.get()
    gender=gender_entry.get()
    national_id=national_id_entry.get()
    driver_license_expiry=driver_license_expiry_date_entry.get() #date YYYY-MM-DD
    license_plate=license_plate_entry.get() #7
    bus_license_expiry=bus_license_expiry_date_entry.get() #date YYYY-MM-DD
    
    if driver_license_expiry=="YYYY-MM-DD":
        driver_license_expiry=""
    if bus_license_expiry=="YYYY-MM-DD":
        bus_license_expiry=""
        
   
        
    if not(first_name.strip() and last_name.strip() and telephone_number.strip() and gender.strip() and national_id.strip() and driver_license_expiry.strip() and license_plate.strip() and bus_license_expiry.strip()):
        messagebox.showerror("Sign Up failed","All fields are required!")
    else:
        try:
            telephone_number=formatTelephone(telephone_number)
            gender=formatGender(gender)
            checkAllDriverEntries(first_name,last_name,telephone_number,gender,national_id,driver_license_expiry,license_plate,bus_license_expiry)
            insertDriverIntoDB(first_name,last_name,telephone_number,gender,national_id,driver_license_expiry,license_plate,bus_license_expiry)
            getDrivers(tree)
            messagebox.showinfo("Success","Added Driver: "+first_name+" "+last_name)
            
            
            first_name_entry.delete('0','end')
            last_name_entry.delete('0','end')
            telephone_number_entry.delete('0','end')
            gender_entry.delete('0','end')
            national_id_entry.delete('0','end')
            driver_license_expiry_date_entry.delete('0','end')
            license_plate_entry.delete('0','end')
            bus_license_expiry_date_entry.delete('0','end')
            bus_license_expiry_date_entry.focus()
            driver_license_expiry_date_entry.focus()
            first_name_entry.focus()
            print("Log: ",first_name," ",last_name," ",telephone_number," ",driver_license_expiry," ",bus_license_expiry)
        except ValueError as error_message:
            messagebox.showerror("Failed to Add: ",error_message)
            
            
def updateDriver(tree,first_name_entry,last_name_entry,telephone_number_entry,gender_entry,national_id_entry,driver_license_expiry_date_entry,license_plate_entry,bus_license_expiry_date_entry):
    first_name=first_name_entry.get()
    last_name=last_name_entry.get()
    telephone_number=telephone_number_entry.get()
    gender=gender_entry.get()
    national_id=national_id_entry.get()
    driver_license_expiry=driver_license_expiry_date_entry.get() #date YYYY-MM-DD
    license_plate=license_plate_entry.get() #7
    bus_license_expiry=bus_license_expiry_date_entry.get()
    
    driver_license_expiry_placeholder=False;
    bus_license_expiry_placeholder=False;
    
    if driver_license_expiry=="YYYY-MM-DD":
        driver_license_expiry=""
        driver_license_expiry_placeholder=True
    if bus_license_expiry=="YYYY-MM-DD":
        bus_license_expiry=""
        bus_license_expiry_placeholder=True
    
    first_name_entry.delete('0','end')
    last_name_entry.delete('0','end')
    telephone_number_entry.delete('0','end')
    gender_entry.delete('0','end')
    national_id_entry.delete('0','end')
    if not driver_license_expiry_placeholder:
        driver_license_expiry_date_entry.delete('0','end')
    license_plate_entry.delete('0','end')
    if not bus_license_expiry_placeholder:
        bus_license_expiry_date_entry.delete('0','end')
    bus_license_expiry_date_entry.focus()
    driver_license_expiry_date_entry.focus()
    first_name_entry.focus()
    
    try:
        selected_item = tree.selection()[0]
        values=tree.item(selected_item,'values')   
        if first_name.strip()=="":
                 first_name=values[2].split()[0]
        if last_name.strip()=="":
                 last_name=values[2].split()[1];  
        if telephone_number.strip()=="":
                 telephone_number=values[3]              
        if gender.strip()=="":
                  gender=values[4]              
        if national_id.strip()=="": 
                  national_id=values[5]             
        if driver_license_expiry.strip()=="": 
                  driver_license_expiry=values[6]            
        if license_plate.strip()=="":
                   license_plate=values[7]               
        if bus_license_expiry.strip()=="": 
                  bus_license_expiry=values[8]
        cursor.execute(
            ''' UPDATE DRIVER SET FIRSTNAME=?,LASTNAME=?,TELEPHONENUM=?,
            GENDER=?,NATIONALID=?,DRIVERLICENSEEXPIRYDATE=?
            WHERE DRIVER.DRIVERID=?;
            UPDATE COMMUTERBUS SET LICENSEPLATE=?,LICENSEEXPIRYDATE=?
            WHERE COMMUTERBUS.DRIVERID=?
            ''',first_name,last_name,telephone_number,gender,national_id,driver_license_expiry,values[0]
            ,license_plate,bus_license_expiry,values[0]
        )
        cursor.commit()
        getDrivers(tree)         
        
    except Exception as e:
        print(e)
    
def deleteDriver(tree):
    try:
       selected_item = tree.selection()[0]
       values=tree.item(selected_item,'values')
       cursor.execute('DELETE DRIVER WHERE DRIVERID=?',values[0])
       cursor.commit()
       getDrivers(tree)
    except Exception as e:
        print(e)
                
