import pyodbc 
from tkinter import messagebox
from re import *
import datetime
from decouple import config
# Establshing connection with mssql
conn = pyodbc.connect(config('DB_CONNECTION'))
cursor = conn.cursor()


def getSessionBookingID():
    cursor.execute("SELECT ISNULL((SELECT MAX(Bookingid) FROM BOOKS_A), -1)")
    session_booking_id = cursor.fetchone()[0]
    return session_booking_id + 1

def checkTripIsBooked(tripId, clientId):
    cursor.execute("SELECT ISNULL((SELECT TRIPID FROM BOOKS_A WHERE TRIPID = ? AND CLIENTID = ?), -1)",tripId,clientId)
    return cursor.fetchone()[0]
    
    
def getTrips(tree):
    cursor.execute("SELECT COUNT(*) FROM trip")
    countOfTrips=cursor.fetchone()
    cursor.execute("""SELECT TripID,TRIP.RouteID,PickupStation,PickupTime,AvailableSeats,TripStatus,TripFee 
                    FROM TRIP inner join ROUTE
                    ON ROUTE.ROUTEID=TRIP.ROUTEID WHERE TRIPSTATUS='Not Completed'""")
    cell_colors=["cell1","cell2"]
    color_index=0
    tree.delete(*tree.get_children())
    for i in range(countOfTrips[0]):
            tripData=cursor.fetchone()
            if(tripData):
                tree.insert('', 'end',text="1", values=(tripData[0],tripData[1],tripData[2],tripData[3],tripData[4],tripData[5],tripData[6]), tags=(cell_colors[color_index]))
            if color_index==0:
                    color_index+=1
            elif color_index==1:
                    color_index-=1;

def getBookings(tree,clientID):
    cursor.execute("""SELECT COUNT(*) FROM BOOKS_A WHERE CLIENTID=?""",clientID)
    countOfTrips=cursor.fetchone()
    cursor.execute("""SELECT BOOKINGID,BOOKS_A.TRIPID,PICKUPSTATION,TRIP.ROUTEID,PickupTime,TripStatus,FIRSTNAME,LASTNAME,LICENSEPLATE,TELEPHONENUM,TripFee,NUMBEROFSEATS,DRIVERRATING,TRIPRATING,TRIP.DRIVERID
                    FROM BOOKS_A inner join TRIP 
                    ON TRIP.TRIPID=BOOKS_A.TRIPID AND BOOKS_A.CLIENTID=?
                    Left outer join DRIVER
                    ON TRIP.DRIVERID=DRIVER.DRIVERID
                    inner join ROUTE
                    ON TRIP.ROUTEID=ROUTE.ROUTEID
                    LEFT join COMMUTERBUS
                    ON DRIVER.DRIVERID = COMMUTERBUS.DRIVERID
                    LEFT OUTER JOIN FEEDBACK
                    ON BOOKS_A.CLIENTID=FEEDBACK.CLIENTID AND BOOKS_A.TRIPID=FEEDBACK.TRIPID""",clientID)
    cell_colors=["cell1","cell2"]
    color_index=0
    tree.delete(*tree.get_children())
    for i in range(countOfTrips[0]):
            bookingData=cursor.fetchone()
            if(not bookingData[14]):
                tree.insert('', 'end',text="1", values=(bookingData[0],bookingData[1],bookingData[2],bookingData[3],bookingData[4],bookingData[5],"___"+" "+"___","___","___",bookingData[10]*bookingData[11],bookingData[11],bookingData[12],bookingData[13]), tags=(cell_colors[color_index]))
            else:
                tree.insert('', 'end',text="1", values=(bookingData[0],bookingData[1],bookingData[2],bookingData[3],bookingData[4],bookingData[5],bookingData[6]+" "+bookingData[7],bookingData[8],bookingData[9],bookingData[10]*bookingData[11],bookingData[11],bookingData[12],bookingData[13]), tags=(cell_colors[color_index]))
            if color_index==0:
                    color_index+=1
            elif color_index==1:
                    color_index-=1;


def bookTrip(tree,clientId,booking_id,numOfSeats):
    try:
       if(len(tree.selection())==0):
            raise ValueError("Please select a Trip")
       selected_item = tree.selection()[0]
       values = tree.item(selected_item,'values')
       isBooked = checkTripIsBooked(values[0],clientId)
       isCompleted = values[5]
       if(isCompleted != "Completed"):
            if(isBooked == -1):
                if(numOfSeats > 0 and numOfSeats <= int(values[4])):
                    cursor.execute('INSERT INTO BOOKS_A VALUES(?,?,?,?)',booking_id,clientId,values[0],numOfSeats)
                    cursor.commit()
                    cursor.execute('UPDATE TRIP SET AVAILABLESEATS = AVAILABLESEATS - ? where TRIPID = ?', numOfSeats,values[0])
                    cursor.commit()
                    getTrips(tree)
                else:
                    raise ValueError("The available seats in this trip is not enough.")
            else:
                raise ValueError("Trip already booked.")
                
       else:
            raise ValueError("Cannot book a completed trip")
    except Exception as e:
        if(str(e)=="Cannot book a completed trip" or str(e)=="Trip already booked." or str(e)=="The available seats in this trip is not enough." or str(e)=="Please select a Trip"):
            print(e)
            messagebox.showinfo("Booking failed",e)

def deleteBooking(tree,clientId):
    try:
        if(len(tree.selection())==0):
            raise ValueError("Please select a Trip Booking")
        selected_item = tree.selection()[0]
        values=tree.item(selected_item,'values')
        isCompleted = values[5]
        if(isCompleted != "Completed"):
            cursor.execute('DELETE FROM BOOKS_A WHERE BOOKINGID = ? AND TRIPID = ?',values[0],values[1])
            cursor.commit()
            cursor.execute('UPDATE TRIP SET AVAILABLESEATS = AVAILABLESEATS + ? where TRIPID = ?',values[10],values[1])
            cursor.commit()
            getBookings(tree,clientId)
        else:
            raise ValueError("Cannot delete booking of a completed trip")
    except Exception as e:
        messagebox.showerror("Booking deletion failed",e)

def giveRating(tree,clientId,driver_rate_entry,trip_rate_entry):
    try:
        if(len(tree.selection())==0):
            raise ValueError("Please select a completed trip of yours")
        selected_item = tree.selection()[0]
        values = tree.item(selected_item,'values')
        tripStatus = values[5]
        # values[1] tripID
        cursor.execute("SELECT COUNT(*) FROM (SELECT * FROM FEEDBACK WHERE CLIENTID=? AND TRIPID=?)as cr",clientId,values[1])
        if(driver_rate_entry.get()==""or trip_rate_entry.get()==""):
            raise ValueError("Please add a rating (1 to 5) for both")
        if(cursor.fetchone()[0]>0):
            raise ValueError("Already rated")
        if(int(driver_rate_entry.get())>5 or int(trip_rate_entry.get())>5 or int(driver_rate_entry.get())<1 or int(trip_rate_entry.get())<1 ):
            raise ValueError("Not a valid rating")
            
        if(tripStatus == "Completed"):
            cursor.execute("""INSERT INTO FEEDBACK
                            VALUES(?,?,?,?)""",clientId,values[1],driver_rate_entry.get(),trip_rate_entry.get())
            cursor.commit()   
            getBookings(tree,clientId)
        else:   
            raise ValueError("Trip not completed!")
    except Exception as e:
        messagebox.showinfo("Failed to give a rating",e)
        
def refreshClientsMainPage(treeTrip,treeBooking,clientID):
    getTrips(treeTrip)
    getBookings(treeBooking,clientID)