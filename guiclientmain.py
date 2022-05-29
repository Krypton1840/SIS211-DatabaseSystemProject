from tkinter import *
from tkinter import ttk, Button, Label,font
from clientmain import *
from pathlib import Path
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
   
class ClientMainPage:
    def __init__(self,id):
        window = Tk()
        window.title("Waddy Client Main Page")
        client_id=id;
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
        
        canvas.create_rectangle(0, 384-45+20, 1448, 385-45+20, fill="#d3d3d3", outline = '#d3d3d3')
                
        style = ttk.Style()

        
        style.configure('Treeview.Heading', background="#ffffff",foreground="#4D47C3",font=('Segoe UI',8,'bold'))
        style.configure('Treeview', background="#ffffff",font=('Segoe UI',7))
        # reload button
        reload_loaded_image=Image.open(relative_to_assets("reload-button.png"))
        reload_loaded_image_resized=reload_loaded_image.resize((35-10,30-10))
        reload_photo = ImageTk.PhotoImage(reload_loaded_image_resized)
        reload_button = Button(image=reload_photo,borderwidth=0,command=lambda:reloadClientsMainPage(tripTree,bookingTree,client_id),relief="flat")
        reload_button.place(x=2.5,y=2.5,width=30-10,height=30-10)
        # Defining fonts
        mainButtonFont= font.Font(family='Segoe UI', size=8, weight='bold')
        mainEntryLabelFont= font.Font(family='Segoe UI', size=8, weight='bold')
        mainEntryFont= font.Font(family='Segoe UI', size=8)

        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        style.configure("Vertical.Scrollbar", background="#FFFFFF", bordercolor="#FFFFFF", arrowcolor="#4D47C3")
        
        # Add a Treeview widget
        canvas.create_text(310+18+100+5-35-100-15,4.5+357+10+3,anchor="nw",text="Upcoming Available Trips",fill="#4D47C3",font=("Segoe UI", 12,'bold'))
        canvas.create_text(310+720-20,4.5+357+10+40,anchor="nw",text="Booking",fill="#4D47C3",font=("Segoe UI", 14,'bold'))
        tripTree = ttk.Treeview(window, column=( "trip_id","route_id","pickup_station","pickup_time","available_seats","trip_status","trip_fee"), show='headings', height=10)
        tripTree.tag_configure('cell1', background='#ededf9')
        tripTree.tag_configure('cell2', background='#dbdaf3')
        
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

        getTrips(tripTree)   #fetching the data

        tripTree.place(x=170-165+20,y=50+290+30-20+10+25+20,width=700,height=300-25)
        scrollTrip = ttk.Scrollbar(window, orient="vertical", command=tripTree.yview)
        scrollTrip.place(x=868-165+20, y=50+290+30-20+10+25+20, height=285+15-25)


        tripTree.configure(yscrollcommand=scrollTrip.set)

        #--------------------------BOOKINGS------------------------------
        canvas.create_text(321+235+10,4.5,anchor="nw",text="Your Trip Bookings",fill="#4D47C3",font=("Segoe UI", 10,'bold'))
        bookingTree = ttk.Treeview(window, column=( "booking_id","trip_id","pickup_station","route_id","pickup_time","trip_status","driver_name","license_plate","telephone_number","trip_fee","number_of_seats","driver_rating","trip_rating"), show='headings', height=10)
        bookingTree.tag_configure('cell1', background='#ededf9')
        bookingTree.tag_configure('cell2', background='#dbdaf3')

        bookingTree.column("booking_id", anchor = CENTER, minwidth=0, width=80,stretch=NO)
        bookingTree.heading("booking_id", text="Booking ID",)

        bookingTree.column("trip_id", anchor = CENTER, minwidth=0, width=80,stretch=NO)
        bookingTree.heading("trip_id", text="Trip ID",)

        bookingTree.column("pickup_station", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("pickup_station", text="Pickup Station",)

        bookingTree.column("route_id", anchor = CENTER, minwidth=0, width=70,stretch=NO)
        bookingTree.heading("route_id", text="Route ID",)

        bookingTree.column("pickup_time", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("pickup_time", text="Pickup time",)

        bookingTree.column("trip_status", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("trip_status", text="Trip Status",)

        bookingTree.column("driver_name", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("driver_name", text="Driver Name",)

        bookingTree.column("license_plate", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("license_plate", text="License Plate",)

        bookingTree.column("telephone_number", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("telephone_number", text="Telephone No.",)

        bookingTree.column("trip_fee", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("trip_fee", text="Trip Fee",)

        bookingTree.column("number_of_seats", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        bookingTree.heading("number_of_seats", text="Number Of Seats",)

        bookingTree.column("driver_rating", anchor = CENTER, minwidth=0, width=80,stretch=NO)
        bookingTree.heading("driver_rating", text="Driver Rating",)

        bookingTree.column("trip_rating", anchor = CENTER, minwidth=0, width=80,stretch=NO)
        bookingTree.heading("trip_rating", text="Trip Rating",)
    
        bookingTree.place(x=170-165+20,y=50-20,width=1200,height=300-20-20)
        scrollBooking = ttk.Scrollbar(window, orient="vertical", command=bookingTree.yview)
        scrollBooking.place(x=1400+20-206.5, y=50-20, height=285+15-20-20)

        bookingTree.configure(yscrollcommand=scrollBooking.set)
        getBookings(bookingTree,client_id)

        canvas.create_text(800+170-60+100-3,181.0+175+105,anchor="nw",text="Number of seats",fill="#4D47C3",font=mainEntryLabelFont)
        number_of_seats_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        number_of_seats_entry.place(x=800+170-60+100-25,y=202.0+175+105+4,width=130.0,height=20.0)
        
        def booking(tripTree,client_id,bookingTree,numberOfSeats):
            if(numberOfSeats.get()==""):
                bookTrip(tripTree,client_id,session_booking_id,1)
            else:
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
        book_trip_button.place(x=950-40+100,y=202.0+170+105+50,width=109.0-30,height=32.0)
        delete_booking_button = Button(text='Delete Trip Booking',bg='#960f00',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:deletebooking(tripTree,client_id,bookingTree),
                               relief="flat"
                        )
        delete_booking_button.place(x=1050-63,y=202.0+107,width=109.0+10,height=32.0)  


        canvas.create_text(800-330-28,181.0+185+50+50+40+40-215-5-10-15,anchor="nw",text="Trip Rating (1 to 5)",fill="#4D47C3",font=mainEntryLabelFont)
        trip_rate_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        trip_rate_entry.place(x=800-330-28,y=202.0+185+50+50+40+40-215-5-10-15,width=130.0,height=20.0)

        
        canvas.create_text(950-330-28,181.0+185+50+50+40+40-215-5-10-15,anchor="nw",text="Driver Rating (1 to 5)",fill="#4D47C3",font=mainEntryLabelFont)
        driver_rate_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        driver_rate_entry.place(x=950-330-28,y=202.0+185+50+50+40+40-215-5-10-15,width=130.0,height=20.0)

        rate_button = Button(text='Give Rating',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:giveRating(bookingTree,client_id,driver_rate_entry,trip_rate_entry),
                               relief="flat"
                        )

        rate_button.place(x=1100-330-28,y=202.0+107,width=109.0-30,height=32.0) 
        
        
        def redirectToProfile():
            window.destroy()
            import guiclientprofile
            guiclientprofile.ViewClientProfilePage(client_id)

        go_to_profile_button = Button(text='Go to your profile',bg='#FAF9F6',fg='#4D47C3',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:redirectToProfile(),
                               relief="flat"
                        )

        go_to_profile_button.place(x=320+900+25,y=13,width=100.0,height=32.0)   

        window.mainloop()
        
