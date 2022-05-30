import pyodbc 
from tkinter import messagebox
from re import *
from datetime import datetime,timedelta
from decouple import config

from adminreport import generateTelephoneNumReportOfCancelled, generateTelephoneNumReportOfRouteInOp
conn = pyodbc.connect(config('DB_CONNECTION'))
cursor = conn.cursor()

def getAdminName(admin_id):
    cursor.execute("SELECT FirstName,LastName FROM Admin WHERE AdminID=?",admin_id)
    adminName=cursor.fetchone()
    return adminName[0]+" "+adminName[1]

def generateTrips(tree):
    
    # If no drivers is the db
    cursor.execute("SELECT COUNT(*) FROM DRIVER");
    number_of_drivers=cursor.fetchone()[0]
    if(number_of_drivers==0):
        messagebox.showerror("Failed to Generate Trips", "You didn't register any driver")
        return -1;
    
    # if there is a trip of status not completed
    cursor.execute("SELECT COUNT(*) FROM TRIP WHERE TRIPSTATUS='Not Completed'");
    number_of_not_completed=cursor.fetchone()[0]
    if(number_of_not_completed>0):
        messagebox.showerror("Failed to Generate Trips", "You can't generate trips if there are trips of status not completed. Either mark them as completed or cancel them if there is an issue")
        return -1;
    
    
    # if there is operative route
    cursor.execute("SELECT COUNT(1) FROM Route WHERE Operative=1")
    is_one_route_operative=cursor.fetchone()[0]
    if is_one_route_operative==0:
        messagebox.showerror("Failed to Generate Trips", "Routes are InOperative right now")
        return -1
    
    
    # Getting the operative routes
    cursor.execute("SELECT RouteID FROM ROUTE WHERE Operative=1")
    operative_routes=[]
    for row in cursor:
        operative_routes.append(row[0])
        
        
    #-------------------------------------------------------------------------------------------------------------------------------------------
    
    
    cursor.execute(""" SELECT COUNT(*) FROM (SELECT DRIVERID FROM DRIVER EXCEPT SELECT TRIP.DRIVERID FROM TRIP) as d
                   
                   """)
    count_of_new_available_drivers=cursor.fetchone()[0]
    
    cursor.execute(""" SELECT DRIVERID FROM DRIVER EXCEPT SELECT TRIP.DRIVERID FROM TRIP
                   
                   """)
    new_available_drivers=cursor.fetchall()
    
    
    
    #-------------------------------------------------------------------------------------------------------------------------------------------
    
    cursor.execute("""SELECT MAX(TripID) as TripID ,TRIP.DRIVERID FROM DRIVER INNER JOIN TRIP ON Driver.DriverID=Trip.DriverID GROUP BY TRIP.DRIVERID""");
    max_trip_of_all=cursor.fetchall()
    previously_worked_but_available_drivers=[]
    count_of_previously_worked_but_available_drivers=0;
    for row in max_trip_of_all:
        cursor.execute("SELECT COUNT(*) FROM (SELECT DRIVERID,ROUTEID,TRIPID FROM TRIP where TRIPID=? AND TripStatus='Completed') as cmax",row[0])
        if cursor.fetchone()[0]==1:
            cursor.execute("SELECT DRIVERID,ROUTEID,TRIPID FROM TRIP where TRIPID=? AND TripStatus='Completed'",row[0])
            previously_worked_but_available_drivers.append(cursor.fetchone())
            count_of_previously_worked_but_available_drivers+=1
    
    all_available_drivers=[]
    
    if count_of_previously_worked_but_available_drivers==0 and count_of_new_available_drivers==0:
        
        messagebox.showerror("Failed to Generate Trips", "No Available Drivers and Commuters")
        return -1;
    
    if count_of_previously_worked_but_available_drivers!=0 and count_of_new_available_drivers==0:
        for i in previously_worked_but_available_drivers:
            all_available_drivers.append(i)
    
    elif count_of_previously_worked_but_available_drivers==0 and count_of_new_available_drivers!=0:
        for i in new_available_drivers:
            all_available_drivers.append((i[0],'X')) 
        
       
    elif count_of_previously_worked_but_available_drivers!=0 and count_of_new_available_drivers!=0:
        for i in previously_worked_but_available_drivers:
            all_available_drivers.append(i) 
        for i in new_available_drivers:
            all_available_drivers.append((i[0],'X')) 
            
    #-------------------------------------------------------------------------------------------------------------------------------------------------------
    starthour=6
    
    trip_status='Not Completed'
    trip_fee=15
    number_of_seats=14
    index=0;
    for i in range(len(all_available_drivers)):
        all_available_drivers[i]=list(all_available_drivers[i])
        
    for row in all_available_drivers:
        if row[1]=="O25":
            all_available_drivers[index][1]="52O"
        elif row[1]=="52O":
            all_available_drivers[index][1]="O25"
        elif row[1]=="X":
            if index%2==0:
               all_available_drivers[index][1]="O25"
            else:
               all_available_drivers[index][1]="52O"
        index+=1 
               
    drivers_of_O25=[]
    drivers_of_52O=[]
    for row in all_available_drivers:
        if row[1]=="O25":
            drivers_of_O25.append(row);
        elif row[1]=="52O":
            drivers_of_52O.append(row);
        
    if(len(drivers_of_52O)==0 and "52O" in operative_routes):
        messagebox.showwarning("Important Note","There will be no 52O trips as there is no drivers and commuter buses resting at the 5th Settlement station.")
        
    if(len(drivers_of_O25)==0 and "O25" in operative_routes):
        messagebox.showwarning("Important Note","There will be no O25 trips as there is no drivers and commuter buses resting at the 6th October station.")
    if(len(drivers_of_52O)==0 and "52O" in operative_routes) and (len(drivers_of_O25)==0 and "O25" in operative_routes):
        return -1;    
    
    if(0<len(drivers_of_52O)<17 and "52O" in operative_routes):
        messagebox.showwarning("Important Note","Not all 52O trips from 6:00 to 22:00 will be available due to shortage of drivers and commuter buses resting at the 5th Settlement station. Only "+str(len(drivers_of_52O))+" trips (starting from 6:00) will be available")
        admin_answer=messagebox.askyesno("","Do you want to proceed and generate only "+str(len(drivers_of_52O))+" 52O trips (starting from 6:00)?")
        if(admin_answer!=True):
            return -1;
    if(0<len(drivers_of_O25)<17 and "O25" in operative_routes):
        messagebox.showwarning("Important Note","Not all O25 trips from 6:00 to 22:00 will be available due to shortage of drivers and commuter buses resting at the 6th October station. Only "+str(len(drivers_of_O25))+" trips (starting from 6:00) will be available")
        admin_answer=messagebox.askyesno("","Do you want to proceed and generate only "+str(len(drivers_of_O25))+" O25 trips (starting from 6:00)?")
        if(admin_answer!=True):
            return -1;
    trip_pickup_time= datetime.strftime(datetime(1,1,1,starthour,0,0,0),"%H:%M")
    for i in range(17):# Number of trips
        trip_pickup_time
        if len(drivers_of_O25)!=0 and i<len(drivers_of_O25) and "O25" in operative_routes: #October
                cursor.execute("""INSERT INTO TRIP(RouteID,DriverID,PickupTime,AvailableSeats,TripStatus,TripFee)
                                              VALUES(?,?,?,?,?,?);""",drivers_of_O25[i][1],drivers_of_O25[i][0],trip_pickup_time,number_of_seats,trip_status,trip_fee)
                cursor.commit()
        if len(drivers_of_52O)!=0 and i<len(drivers_of_52O) and "52O" in operative_routes:
                cursor.execute("""INSERT INTO TRIP(RouteID,DriverID,PickupTime,AvailableSeats,TripStatus,TripFee)
                                              VALUES(?,?,?,?,?,?);""",drivers_of_52O[i][1],drivers_of_52O[i][0],trip_pickup_time,number_of_seats,trip_status,trip_fee)
                cursor.commit()
        trip_pickup_time=datetime.strftime(datetime(1,1,1,int(trip_pickup_time[0:2]),0,0,0)+timedelta(hours=1),"%H:%M")
                
    getTrips(tree)       
        
def cancelTrip(tree):
        try:     
            if(len(tree.selection())==0):
                raise ValueError("Please select a Trip")
            selected_item = tree.selection()[0]
            values=tree.item(selected_item,'values')
            cursor.execute("""SELECT COUNT(*) FROM (SELECT TRIPID FROM TRIP WHERE TRIPID=? AND TRIPSTATUS='Not Completed') as c""",values[0])
            if(cursor.fetchone()[0]!=0):
                clientsExists=generateTelephoneNumReportOfCancelled(values[0])
                cursor.execute("""DELETE FROM TRIP WHERE TRIPID=? AND TRIPSTATUS='Not Completed'
                           """,values[0])
                cursor.commit()
                if(clientsExists==True):
                    messagebox.showwarning("Note","A pdf of the clients and their telephone no. that booked trip "+values[0]+" is generated,Please inform the clients of the cancellation")
                getTrips(tree)
            else:
                raise ValueError("Trip's status is completed so you can't cancel it")
        except Exception as e:
            messagebox.showerror("Cancellation failed",e)
def markTripCompleted(tree):
        try:
            if(len(tree.selection())==0):
                raise ValueError("Please select a Trip")     
            selected_item = tree.selection()[0]
            values=tree.item(selected_item,'values')
            cursor.execute("""UPDATE TRIP SET TripStatus='Completed' WHERE TRIPID=?
                           """,values[0])
            cursor.commit()
            getTrips(tree)
        except Exception as e:
            messagebox.showerror("",e)       
def markAllTripsCompleted(tree):
        try:     
            cursor.execute("""UPDATE TRIP SET TripStatus='Completed'
                           """)
            cursor.commit()
            getTrips(tree)
        except Exception as e:
            print(e)           
    
def makeRouteOperative(tree): #route tree
       try: 
            if(len(tree.selection())==0):
                raise ValueError("Please select a route")
            selected_item = tree.selection()[0]
            values=tree.item(selected_item,'values')
            cursor.execute("""UPDATE ROUTE SET Operative=1 WHERE RouteID=?
                           """,values[0])
            cursor.commit()
            getRoutes(tree)
       except Exception as e:
           messagebox.showerror("",e)
           
def makeRouteInOperative(tree,treeTrip): #route tree
       try: 
            if(len(tree.selection())==0):
                raise ValueError("Please select a route")
            selected_item = tree.selection()[0]
            values=tree.item(selected_item,'values')
            cursor.execute("""UPDATE ROUTE SET Operative=0 WHERE RouteID=?
                           """,values[0])
            cursor.commit()
            
            cursor.execute("""SELECT COUNT(*) FROM (SELECT TRIPID FROM TRIP WHERE TRIP.ROUTEID=? AND TripStatus='Not Completed')as t;
                           """,values[0])
            count_of_canceled_trips=cursor.fetchone()[0]
            if count_of_canceled_trips!=0:
                generateTelephoneNumReportOfRouteInOp(values[0])
                messagebox.showinfo("Note","A pdf of the cancelled trips and if there are clients that booked trips on route "+values[0]+"(theirs names and telephone no. are added to pdf) is generated,Please inform the clients ,if there are any, of the cancellation")
                
            cursor.execute("""DELETE FROM TRIP WHERE RouteID=? AND TripStatus='Not Completed'""",values[0])
            cursor.commit()
            
            getRoutes(tree)
            getTrips(treeTrip)
       except Exception as e:
           messagebox.showerror("",e)
 
    
def getClients(tree): # client tree
           cursor.execute("SELECT COUNT(*) FROM client")
           countOfClients=cursor.fetchone()
           
           cursor.execute('SELECT ClientID,FirstName,LastName,TelephoneNum,Email,Gender from client')
           cell_colors=["cell1","cell2"]
           color_index=0
           tree.delete(*tree.get_children())
           for i in range(countOfClients[0]):
                  clientData=cursor.fetchone()
                  if(clientData):
                    if(clientData[5]==None):  
                        tree.insert('', 'end',text="1", values=(clientData[0],clientData[1]+" "+clientData[2],clientData[3],clientData[4],"___"), tags=(cell_colors[color_index]))
                    else:
                        tree.insert('', 'end', text="1", values=(clientData[0],clientData[1]+" "+clientData[2],clientData[3],clientData[4],clientData[5]), tags=(cell_colors[color_index]))
                    if color_index==0:
                           color_index+=1
                    elif color_index==1:
                           color_index-=1;
                           
def getRoutes(tree):#route tree
    cursor.execute("SELECT RouteId,Operative FROM ROUTE")
    cell_colors=["cell1","cell2"]
    color_index=0
    tree.delete(*tree.get_children())
    for i in range(2):
         routeData=cursor.fetchone()
         if(routeData):
             if routeData[1] == 1:
                 tree.insert('','end',text="1", values=(routeData[0],"Operative"), tags=(cell_colors[color_index]))
             elif routeData[1] == 0:
                 tree.insert('','end',text="1", values=(routeData[0],"InOperative"), tags=(cell_colors[color_index]))
             if color_index==0:
                 color_index+=1
             elif color_index==1:
                 color_index-=1;
         
    
def getTrips(tree):
           cursor.execute("SELECT COUNT(*) FROM trip")
           countOfTrips=cursor.fetchone()
           cursor.execute('SELECT TripID,RouteID,Trip.DriverID,FirstName,LastName,PickupTime,AvailableSeats,TripStatus,TripFee from trip left join driver on trip.DriverID=driver.DriverID order by TripID;')
           cell_colors=["cell1","cell2"]
           color_index=0
           tree.delete(*tree.get_children())
           
           for i in range(countOfTrips[0]):
                  tripData=cursor.fetchone()
                  if(tripData):
                    if(not tripData[2]):
                        if(str(tripData[5])=="06:00:00"):
                            tree.insert('', 'end',text="1", values=(tripData[0],tripData[1],"___","___",tripData[4+1],tripData[5+1],tripData[6+1],tripData[7+1]), tags=("cellstart"))
                        else:    
                            tree.insert('', 'end',text="1", values=(tripData[0],tripData[1],"___","___",tripData[4+1],tripData[5+1],tripData[6+1],tripData[7+1]), tags=(cell_colors[color_index]))
                    else:
                        if(str(tripData[5])=="06:00:00"):
                            tree.insert('', 'end',text="1", values=(tripData[0],tripData[1],tripData[2],tripData[2+1]+" "+tripData[3+1],tripData[4+1],tripData[5+1],tripData[6+1],tripData[7+1]), tags=("cellstart"))
                        else:    
                            tree.insert('', 'end',text="1", values=(tripData[0],tripData[1],tripData[2],tripData[2+1]+" "+tripData[3+1],tripData[4+1],tripData[5+1],tripData[6+1],tripData[7+1]), tags=(cell_colors[color_index]))
                    if color_index==0:
                           color_index+=1
                    elif color_index==1:
                           color_index-=1;
           tree.yview_moveto(1)
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
def refreshAdminMainPage(treeTrip,treeClient,treeDriverBus):
    getTrips(treeTrip)
    getClients(treeClient)
    getDrivers(treeDriverBus)


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
        if(len(tree.selection())==0):
                raise ValueError("Please select a driver")
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
        telephone_number=formatTelephone(telephone_number)
        gender=formatGender(gender)
        checkAllDriverEntries(first_name,last_name,telephone_number,gender,national_id,driver_license_expiry,license_plate,bus_license_expiry)
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
        messagebox.showerror("Update failed",e)
    
def deleteDriver(tree,treeTrip):
    try:
       if(len(tree.selection())==0):
                raise ValueError("Please select a driver")
       selected_item = tree.selection()[0]
       values=tree.item(selected_item,'values')
       cursor.execute("SELECT COUNT(*) FROM (SELECT TRIPID FROM TRIP WHERE TRIP.DRIVERID=? AND TRIP.TRIPSTATUS='Not Completed') as t",values[0])
       has_incomplete_trips=True
       count_of_incomplete_trips=cursor.fetchone()[0]
       
       cancelled_trip_id=-1
       report_generation_success=False
       
       if(count_of_incomplete_trips==0):
           has_incomplete_trips=False
       if(count_of_incomplete_trips==1):
           has_incomplete_trips=True
           cursor.execute("SELECT TRIPID FROM TRIP WHERE TRIP.DRIVERID=? AND TRIP.TRIPSTATUS='Not Completed'",values[0])
           cancelled_trip_id=cursor.fetchone()[0]
           report_generation_success=generateTelephoneNumReportOfCancelled(cancelled_trip_id)
    
           cursor.execute("DELETE TRIP WHERE TRIP.DRIVERID=? AND TRIP.TRIPSTATUS='Not Completed'",values[0])
           cursor.commit()
       cursor.execute('DELETE DRIVER WHERE DRIVERID=?',values[0])
       cursor.commit()
       cursor.execute("""UPDATE TRIP SET DRIVERID=0 WHERE DRIVERID=? AND TRIPSTATUS='Completed'""",values[0])
       cursor.commit()
       if(has_incomplete_trips==True and report_generation_success==True and cancelled_trip_id!=-1 and count_of_incomplete_trips==1):
           messagebox.showwarning("Note","A pdf of the clients and their telephone no. that booked the latest trip of driver of id: "+values[0]+" and the trip is of id: "+str(cancelled_trip_id)+" is generated ,Please inform the clients of the cancellation")
       getDrivers(tree)
       getTrips(treeTrip)
    except Exception as e:
        messagebox.showerror("Deletion failed",e)
                
