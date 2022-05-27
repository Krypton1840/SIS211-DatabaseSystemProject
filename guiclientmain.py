from tkinter import *
from tkinter import ttk, Button, Label,font
from clientmain import *

   
class ClientMainPage:
    def __init__(self,id):
        window = Tk()
        window.title("Waddy Client Main Page")
        client_id=id[0];
        session_booking_id = getSessionBookingID()
        
        window.geometry("1448x768")
        window.configure(bg = "#FFFFFF")
        canvas = Canvas(
            window,
            bg = "#FAF9F6",
            height = 768,
            width = 1448,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        
        # x=868-165+95+20, y=50+290+30-20,
        canvas.create_rectangle(0, 384-45, 1448, 385-45, fill="#d3d3d3", outline = '#d3d3d3')
                
        style = ttk.Style()

        # style.theme_use('clam')
        style.configure('Treeview.Heading', background="#ffffff",foreground="#4D47C3",font=('Segoe UI',8,'bold'))
        style.configure('Treeview', background="#ffffff",font=('Segoe UI',7))

        # Defining fonts
        mainButtonFont= font.Font(family='Segoe UI', size=7, weight='bold')
        mainEntryLabelFont= font.Font(family='Segoe UI', size=8, weight='bold')
        mainEntryFont= font.Font(family='Segoe UI', size=8)

        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        style.configure("Vertical.Scrollbar", background="#FFFFFF", bordercolor="#FFFFFF", arrowcolor="#4D47C3")
        
        # Add a Treeview widget
        tripTree = ttk.Treeview(window, column=( "trip_id","route_id","pickup_station","pickup_time","available_seats","trip_status","trip_fee"), show='headings', height=10)
        tripTree.tag_configure('cell1', background='#ededf9')
        tripTree.tag_configure('cell2', background='#dbdaf3')
        
        # "driver_name",
        # "pickup_time",
        # "available_seats",
        # "trip_fee"
        tripTree.column("trip_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        tripTree.heading("trip_id", text="Trip ID",)

        tripTree.column("route_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        tripTree.heading("route_id", text="Route ID",)

        tripTree.column("pickup_station", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        tripTree.heading("pickup_station", text="Pickup Station",)

        tripTree.column("pickup_time", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        tripTree.heading("pickup_time", text="Pickup Time",)

        tripTree.column("available_seats", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        tripTree.heading("available_seats", text="Available Seats",)

        tripTree.column("trip_status", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        tripTree.heading("trip_status", text="Trip Status",)

        tripTree.column("trip_fee", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        tripTree.heading("trip_fee", text="Trip Fee",)

        # "pickup_time",
        # "available_seats",
        # "trip_fee"
        
        getTrips(tripTree)   #fetching the data

        tripTree.place(x=170-165+20,y=50+290+30-20,width=700,height=300)
        scrollTrip = ttk.Scrollbar(window, orient="vertical", command=tripTree.yview)
        scrollTrip.place(x=868-165+20, y=50+290+30-20, height=285+15)


        tripTree.configure(yscrollcommand=scrollTrip.set)

        #--------------------------BOOKINGS------------------------------
        bookingTree = ttk.Treeview(window, column=( "booking_id","trip_id","pickup_station","route_id","pickup_time","trip_status","driver_name","gender","license_plate","telephone_number","trip_fee","number_of_seats","driver_rating","trip_rating"), show='headings', height=10)
        bookingTree.tag_configure('cell1', background='#ededf9')
        bookingTree.tag_configure('cell2', background='#dbdaf3')

        bookingTree.column("booking_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("booking_id", text="Booking ID",)

        bookingTree.column("trip_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("trip_id", text="Trip ID",)

        bookingTree.column("pickup_station", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("pickup_station", text="Pickup Station",)

        bookingTree.column("route_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("route_id", text="Route ID",)

        bookingTree.column("pickup_time", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("pickup_time", text="Pickup time",)

        bookingTree.column("trip_status", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("trip_status", text="Trip Status",)

        bookingTree.column("driver_name", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("driver_name", text="Driver Name",)

        bookingTree.column("gender", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("gender", text="Gender",)

        bookingTree.column("license_plate", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("license_plate", text="License Plate",)

        bookingTree.column("telephone_number", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("telephone_number", text="Telephone No.",)

        bookingTree.column("trip_fee", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("trip_fee", text="Trip Fee",)

        bookingTree.column("number_of_seats", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("number_of_seats", text="Number Of Seats",)

        bookingTree.column("driver_rating", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("driver_rating", text="Driver Rating",)

        bookingTree.column("trip_rating", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("trip_rating", text="Trip Rating",)

        bookingTree.place(x=170-165+20,y=50-20,width=1400,height=300)
        scrollBooking = ttk.Scrollbar(window, orient="vertical", command=bookingTree.yview)
        scrollBooking.place(x=1400+20, y=50-20, height=285+15)

        bookingTree.configure(yscrollcommand=scrollBooking.set)
        getBookings(bookingTree,client_id)

        canvas.create_text(800,181.0+175,anchor="nw",text="Number of seats",fill="#4D47C3",font=mainEntryLabelFont)
        number_of_seats_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        number_of_seats_entry.place(x=800,y=202.0+175,width=130.0,height=20.0)
        
        def booking(tripTree,client_id,bookingTree,numberOfSeats):
            bookTrip(tripTree,client_id,session_booking_id,int(numberOfSeats.get()))
            getBookings(bookingTree,client_id)

        def deletebooking(tripTree,client_id,bookingTree):
            deleteBooking(bookingTree,client_id)
            getTrips(tripTree)
        
        # Buttons and entries

        book_trip_button = Button(text='Book Trip',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:booking(tripTree,client_id,bookingTree,number_of_seats_entry),
                               relief="flat"
                        )
        book_trip_button.place(x=950,y=202.0+170,width=109.0-30,height=32.0)     
        
        delete_booking_button = Button(text='Delete',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:deletebooking(tripTree,client_id,bookingTree),
                               relief="flat"
                        )
        delete_booking_button.place(x=1050,y=202.0+170,width=109.0-30,height=32.0)  


        canvas.create_text(800,181.0+185+50+50+40+40,anchor="nw",text="Trip Rating",fill="#4D47C3",font=mainEntryLabelFont)
        trip_rate_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        trip_rate_entry.place(x=800,y=202.0+185+50+50+40+40,width=130.0,height=20.0)

        
        canvas.create_text(950,181.0+185+50+50+40+40,anchor="nw",text="Driver Rating",fill="#4D47C3",font=mainEntryLabelFont)
        driver_rate_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        driver_rate_entry.place(x=950,y=202.0+185+50+50+40+40,width=130.0,height=20.0)

        rate_button = Button(text='Give Rating',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:giveRating(bookingTree,client_id,driver_rate_entry,trip_rate_entry),
                               relief="flat"
                        )

        rate_button.place(x=1100,y=202.0+185+50+50+72,width=109.0-30,height=32.0)    

        window.mainloop()
