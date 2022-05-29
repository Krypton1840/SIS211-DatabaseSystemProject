from fpdf import FPDF
import pyodbc 
from decouple import config
# Establshing connection with mssql
conn = pyodbc.connect(config('DB_CONNECTION'))
cursor = conn.cursor()
import time

namedtuple=time.localtime()
time_string_title=time.strftime("%m/%d/%Y %H:%M:%S",namedtuple)
time_string=time.strftime("%m-%d-%Y",namedtuple)
class PDF(FPDF):
    def header(self):
        # Logo
        
        # Arial bold 15
        self.set_font('Times', 'B', 25)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10,'Report: '+'%s'%time_string_title, 0, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Times', 'I', 12)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
def generateReport():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '',12)
    cursor.execute("SELECT COUNT(*) FROM TRIP WHERE TRIPSTATUS='Completed'")
    pdf.multi_cell(0,5+5+5,"- Total number of completed trips: "+str(cursor.fetchone()[0]))
    
    cursor.execute("SELECT COUNT(*) FROM TRIP WHERE TRIPSTATUS='Completed' AND ROUTEID='O25'")
    pdf.multi_cell(0,5+5+5,"- Number of completed trips from 6th October To 5th Settlement: "+str(cursor.fetchone()[0]))
    
    cursor.execute("SELECT COUNT(*) FROM TRIP WHERE TRIPSTATUS='Completed' AND ROUTEID='52O'")
    pdf.multi_cell(0,5+5+5,"- Number of completed trips from 5th Settlement To 6th October : "+str(cursor.fetchone()[0]))
    
    cursor.execute("SELECT COUNT(*) FROM DRIVER")
    pdf.multi_cell(0,5+5+5,"- Total number of drivers: "+str(cursor.fetchone()[0]))
    
    cursor.execute("SELECT COUNT(*) FROM COMMUTERBUS")
    pdf.multi_cell(0,5+5+5,"- Total number of commuter buses: "+str(cursor.fetchone()[0]))
    
    cursor.execute("SELECT COUNT(*) FROM CLIENT")
    pdf.multi_cell(0,5+5+5,"- Total number of clients: "+str(cursor.fetchone()[0]))
    
    cursor.execute("SELECT COUNT(*) FROM BOOKS_A")
    pdf.multi_cell(0,5+5+5,"- Total number of Trip bookings: "+str(cursor.fetchone()[0]))
  
    
    cursor.execute("SELECT COUNT(*) FROM FEEDBACK")
    pdf.multi_cell(0,5+5+5,"- Total number of feedbacks given: "+str(cursor.fetchone()[0]))
    
    pdf.multi_cell(0,5+5+5,"- Names of Drivers given maximum driver rating: ")
    cursor.execute("SELECT DISTINCT FIRSTNAME,LASTNAME from FEEDBACK inner join trip on feedback.TRIPID=trip.TRIPID inner join driver on trip.DRIVERID = driver.DRIVERID WHERE DRIVERRATING=5")
    for row in cursor:
        pdf.multi_cell(0,5+5+5,"    + Driver name: "+row[0]+" "+row[1])
    
    pdf.multi_cell(0,5+5+5,"- Client(s) with maximum number of Trip Bookings:")
    cursor.execute("select max(bookingcount) from (select client.clientId,count(client.clientId) bookingcount from BOOKS_A inner join CLIENT on BOOKS_A.CLIENTID=CLIENT.CLIENTID group by client.clientId) as c")
    maxTripBookings=cursor.fetchone()[0]
    
    cursor.execute("select CLIENT.FIRSTNAME,CLIENT.LASTNAME,COUNT(BOOKINGID) from client inner join BOOKS_A on CLIENT.CLIENTID=BOOKS_A.CLIENTID GROUP BY CLIENT.CLIENTID,CLIENT.FIRSTNAME,CLIENT.LASTNAME HAVING COUNT(BOOKINGID)=? ;",maxTripBookings)

    for row in cursor:
        pdf.multi_cell(0,5+5+5,"    + Client name: "+row[0]+" "+row[1]+" No. of Trip Bookings= "+str(row[2]))
    
    pdf.output('Report%s.pdf'%time_string, 'F')
    
    
def generateTelephoneNumReportOfCancelled(trip_id):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '',20)
    # //title
    pdf.multi_cell(0,5+5,"Trip Cancelled: "+str(trip_id))
    pdf.set_font('Times', '',14)
    cursor.execute("""SELECT COUNT(*) FROM (SELECT CLIENT.FIRSTNAME,CLIENT.LASTNAME,CLIENT.TELEPHONENUM FROM 
                               BOOKS_A INNER JOIN CLIENT ON BOOKS_A.CLIENTID = CLIENT.CLIENTID 
                               INNER JOIN TRIP ON BOOKS_A.TRIPID =TRIP.TRIPID WHERE BOOKS_A.TRIPID=? AND TRIPSTATUS='Not Completed') as cl""",trip_id)
    if(cursor.fetchone()[0]==0):
        return False;
    cursor.execute("""SELECT CLIENT.FIRSTNAME,CLIENT.LASTNAME,CLIENT.TELEPHONENUM FROM 
                               BOOKS_A INNER JOIN CLIENT ON BOOKS_A.CLIENTID = CLIENT.CLIENTID 
                               INNER JOIN TRIP ON BOOKS_A.TRIPID =TRIP.TRIPID WHERE BOOKS_A.TRIPID=? AND TRIPSTATUS='Not Completed'""",trip_id)
    for row in cursor:
        pdf.multi_cell(0,5+5,"Client Name : "+row[0]+" "+row[1]+" "+", Telephone no. :"+row[2])
    pdf.output('cancelledtrip'+str(trip_id)+'.pdf', 'F')
    return True
def generateTelephoneNumReportOfRouteInOp(route_id):
    cursor.execute("""SELECT TRIPID FROM TRIP WHERE TRIP.ROUTEID=? AND TripStatus='Not Completed'""",route_id)
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '',20)
    # //title
    pdf.multi_cell(0,5+5,"Route: "+str(route_id))
    arr_trip_id=[]
    for row in cursor:
        arr_trip_id.append(row[0])
        
    for trip_id in arr_trip_id:
        pdf.set_font('Times', '',17)
        # //title
        pdf.multi_cell(0,5+5,"Trip: "+str(trip_id))
        pdf.set_font('Times', '',14)
        cursor.execute("""SELECT COUNT(*) FROM (SELECT CLIENT.FIRSTNAME,CLIENT.LASTNAME,CLIENT.TELEPHONENUM FROM 
                               BOOKS_A INNER JOIN CLIENT ON BOOKS_A.CLIENTID = CLIENT.CLIENTID 
                               INNER JOIN TRIP ON BOOKS_A.TRIPID =TRIP.TRIPID WHERE BOOKS_A.TRIPID=? AND TRIPSTATUS='Not Completed') as cl""",trip_id)
        if(cursor.fetchone()[0]==0):
            continue
        cursor.execute("""SELECT CLIENT.FIRSTNAME,CLIENT.LASTNAME,CLIENT.TELEPHONENUM FROM 
                               BOOKS_A INNER JOIN CLIENT ON BOOKS_A.CLIENTID = CLIENT.CLIENTID 
                               INNER JOIN TRIP ON BOOKS_A.TRIPID =TRIP.TRIPID WHERE BOOKS_A.TRIPID=? AND TRIPSTATUS='Not Completed'""",trip_id)
        for client in cursor:
            pdf.multi_cell(0,5+5,"Client Name : "+client[0]+" "+client[1]+" "+", Telephone no. :"+client[2])
    pdf.output('cancelledTripsRoute'+str(route_id)+'.pdf', 'F')
        
    


    

