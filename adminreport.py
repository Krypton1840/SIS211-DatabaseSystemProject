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
    
    cursor
    
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

    

