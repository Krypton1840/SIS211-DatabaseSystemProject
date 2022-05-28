from tkinter import *
from tkinter import ttk, Button, Label,font
from adminmain import *
from pathlib import Path
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AdminMainPage:
    def __init__(self,id):
        window = Tk()
        window.title("Waddy Admin Main Page")
        admin_id=id;
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
        mainButtonFont= font.Font(family='Segoe UI', size=8, weight='bold')
        #---------------------------------------------------------------------------------------
        reload_loaded_image=Image.open(relative_to_assets("reload-button.png"))
        reload_loaded_image_resized=reload_loaded_image.resize((35-10,30-10))
        reload_photo = ImageTk.PhotoImage(reload_loaded_image_resized)
        reload_button = Button(image=reload_photo,borderwidth=0,command=lambda:reloadAdminMainPage(treeTrip,treeClient,treeDriverBus),relief="flat")
        reload_button.place(x=2.5,y=2.5,width=30-10,height=30-10)
        
        #------------------------------------------------------------------Trips and Routes Toolbox------------------------------------------------------------
        canvas.create_text(321,2.5,anchor="nw",text="Trips and Routes",fill="#4D47C3",font=("Segoe UI", 10,'bold'))
        
        make_operative_bus_button = Button(text='Operative',bg='#018f06',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:makeRouteOperative(treeRoute),
                               relief="flat"
                        )
# x=170-165+20,y=300+20
        make_operative_bus_button.place(x=320-40-60-7,y=320,width=109.0-10,height=25.0)
        
        make_inoperative_bus_button = Button(text='InOperative',bg='#960f00',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:makeRouteInOperative(treeRoute,treeTrip),
                               relief="flat"
                        )
# x=170-165+20,y=300+20
        make_inoperative_bus_button.place(x=320-40-60-7,y=320+35,width=109.0-10,height=25.0)
        
        canvas.create_rectangle(390-60-7, 310, 391-60-7, 320+35+25+10, fill="#d3d3d3", outline = '#d3d3d3')#vertical line trip route tools
        
        
        generate_trips_button = Button(text='Generate Trips',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:generateTrips(treeTrip),
                               relief="flat"
                        )

        generate_trips_button.place(x=320+100-60-23+7,y=320+15,width=109.0,height=32.0)
        
        
        #           !Will generate a pdf with the telephone numbers!
        cancel_trip_button = Button(text='Cancel Trip',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:cancelTrip(treeTrip),
                               relief="flat"
                        )

        cancel_trip_button.place(x=320+140+7,y=320+15,width=109.0,height=32.0)
        
        
        mark_trip_as_completed_button = Button(text='Mark Trip as Completed',bg='#4D47C3',fg='#ffffff',font=('Segoe UI',7,'bold'), borderwidth=0,highlightthickness=0,
                               command=lambda:markTripCompleted(treeTrip),
                               relief="flat"
                        )

        mark_trip_as_completed_button.place(x=320+140+123+7,y=320+15-19,width=139.0,height=32.0)
        
        mark_all_as_completed_button = Button(text='Mark All Trips as Completed',bg='#4D47C3',fg='#ffffff',font=('Segoe UI',7,'bold'), borderwidth=0,highlightthickness=0,
                               command=lambda:markAllTripsCompleted(treeTrip),
                               relief="flat"
                        )

        mark_all_as_completed_button.place(x=320+140+123+7,y=320+15+35-19,width=139.0,height=32.0)
        
        
        canvas.create_rectangle(390-60-7+426+10, 0, 391-60-7+426+10, 320+35+25+14, fill="#d3d3d3", outline = '#d3d3d3')#vertical line trip and user and pdf
        #------------------------------------------------------------------Client box----------------------------------------------------------------------
        canvas.create_text(541.0+300+75+115+10,72,anchor="nw",text="Clients",fill="#4D47C3",font=("Segoe UI", 10,'bold'))
        canvas.create_rectangle(758.5, 37+30, 1448, 38+30, fill="#d3d3d3", outline = '#d3d3d3')
        #------------------------------------------------------------------------------------------------------------------------------------------------
        
        #-----------------------------------------------------------Report and name and go to profile------------------------------------------------------------
        generate_report_button = Button(text='Press to Generate a Report',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:print("Comp"),
                               relief="flat"
                        )

        generate_report_button.place(x=320+460,y=13,width=139.0+30,height=32.0)
        
        go_to_profile_button = Button(text='Go to your profile',bg='#FAF9F6',fg='#4D47C3',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:print("Comp"),
                               relief="flat"
                        )

        go_to_profile_button.place(x=320+900+25,y=13,width=100.0,height=32.0)
        admin_name=getAdminName(admin_id)
        canvas.create_text(1027+30+10,17+5,anchor="nw",text="Admin: "+admin_name,fill="#000000",font=("Segoe UI", 9,))
        canvas.create_text(950+30+10,17+5,anchor="nw",text="ID: "+admin_id,fill="#000000",font=("Segoe UI", 9,))
        
        #------------------------------------------------------------------------------------------------------------------------------------------------------
        canvas.create_rectangle(0, 384-45+55, 1448, 385-45+55, fill="#d3d3d3", outline = '#d3d3d3')
        #-------------------------------------------------------------------Driver Commuter Toolbox------------------------------------------------------------
        canvas.create_text(541.0+300+75+80+30+30+70,181.0+185+40-30+35,anchor="nw",text="Driver and Commuter Bus",fill="#4D47C3",font=("Segoe UI", 10,'bold'))
        mainEntryLabelFont= font.Font(family='Segoe UI', size=8, weight='bold')
        mainEntryFont= font.Font(family='Segoe UI', size=8)
        
        canvas.create_text(541.0+300+75+80+30+30,181.0+185+40+35,anchor="nw",text="First Name",fill="#4D47C3",font=mainEntryLabelFont)
        first_name_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        first_name_entry.place(x=539.0+300+75+80+30+30,y=202.0+185+40+35,width=130.0,height=20.0)
        
        canvas.create_text(541.0+300+75+80+30+30,181.0+185+50+40+35,anchor="nw",text="Last Name",fill="#4D47C3",font=mainEntryLabelFont)
        last_name_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        last_name_entry.place(x=539.0+300+75+80+30+30,y=202.0+185+50+40+35,width=130.0,height=20.0)
        
        canvas.create_text(541.0+300+75+80+30+30,181.0+185+50+50+40+35,anchor="nw",text="Telephone No.",fill="#4D47C3",font=mainEntryLabelFont)
        telephone_number_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        telephone_number_entry.place(x=539.0+300+75+80+30+30,y=202.0+185+50+50+40+35,width=130.0,height=20.0)
        
        canvas.create_text(541.0+300+75+80+30+30,181.0+185+50+50+50+40+35,anchor="nw",text="Gender",fill="#4D47C3",font=mainEntryLabelFont)
        gender_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        gender_entry.place(x=539.0+300+75+80+30+30,y=202.0+185+50+50+50+40+35,width=130.0,height=20.0)
        
        canvas.create_text(541.0+300+190+75+80+30,181.0+185+40+35,anchor="nw",text="National ID",fill="#4D47C3",font=mainEntryLabelFont)
        national_id_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        national_id_entry.place(x=539.0+300+190+75+80+30,y=202.0+185+40+35,width=130.0,height=20.0)
        
        
        def dateEntryFocusOut(Entry):
            if len(Entry.get())==0:
                Entry.insert('0',"YYYY-MM-DD")
        def dateEntryFocusIn(Entry):
            if Entry.get()=="YYYY-MM-DD":
                Entry.delete('0','end')
        
        canvas.create_text(541.0+300+190+75+80+30,181.0+185+50+40+35,anchor="nw",text="Driver License Exp. Date",fill="#4D47C3",font=mainEntryLabelFont)
        driver_license_expiry_date_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        driver_license_expiry_date_entry.place(x=539.0+300+190+75+80+30,y=202.0+185+50+40+35,width=130.0,height=20.0)
        driver_license_expiry_date_entry.insert(0,"YYYY-MM-DD")
        driver_license_expiry_date_entry.bind("<FocusIn>", lambda args: dateEntryFocusIn(driver_license_expiry_date_entry))
        driver_license_expiry_date_entry.bind("<FocusOut>", lambda args: dateEntryFocusOut(driver_license_expiry_date_entry))
        
        
        canvas.create_text(541.0+300+190+75+80+30,181.0+185+50+50+40+35,anchor="nw",text="License Plate",fill="#4D47C3",font=mainEntryLabelFont)
        license_plate_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        license_plate_entry.place(x=539.0+300+190+75+80+30,y=202.0+185+50+50+40+35,width=130.0,height=20.0)
        
        
        
                
        canvas.create_text(541.0+300+190+75+80+30,181.0+185+50+50+50+40+35,anchor="nw",text="Bus License Exp. Date",fill="#4D47C3",font=mainEntryLabelFont)
        bus_license_expiry_date_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        bus_license_expiry_date_entry.place(x=539.0+300+190+75+80+30,y=202.0+185+50+50+50+40+35,width=130.0,height=20.0)
        bus_license_expiry_date_entry.insert(0,"YYYY-MM-DD")
        bus_license_expiry_date_entry.bind("<FocusIn>", lambda args: dateEntryFocusIn(bus_license_expiry_date_entry))
        bus_license_expiry_date_entry.bind("<FocusOut>", lambda args: dateEntryFocusOut(bus_license_expiry_date_entry))
        
        
        
        
        
        
        add_driver_bus_button = Button(text='Add',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:addDriver(treeDriverBus,first_name_entry,last_name_entry,telephone_number_entry,gender_entry,national_id_entry,driver_license_expiry_date_entry,license_plate_entry,bus_license_expiry_date_entry) ,
                               relief="flat"
                        )

        add_driver_bus_button.place(x=531.0+400+60+80,y=555.0+20+40+35,width=109.0-30,height=32.0)

        update_driver_bus_button = Button(text='Update',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:updateDriver(treeDriverBus,first_name_entry,last_name_entry,telephone_number_entry,gender_entry,national_id_entry,driver_license_expiry_date_entry,license_plate_entry,bus_license_expiry_date_entry),
                               relief="flat"
                        )

        update_driver_bus_button.place(x=531.0+488+60+80,y=555.0+20+40+35,width=109.0-30,height=32.0)      
        
        delete_driver_bus_button = Button(text='Delete',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:deleteDriver(treeDriverBus,treeTrip),
                               relief="flat"
                        )

        delete_driver_bus_button.place(x=531.0+488+60+80+88,y=555.0+20+40+35,width=109.0-30,height=32.0)  

        
        #------------------------------------------------------------- Trees ------------------------------------------------------------        
        style = ttk.Style()

        # style.theme_use('clam')
        style.configure('Treeview.Heading', background="#ffffff",foreground="#4D47C3",font=('Segoe UI',8,'bold'))
        
        style.configure('treeRoute.Heading', background="#ffffff",foreground="#4D47C3",font=('Segoe UI',20,'bold'))
        
        style.configure('Treeview', background="#ffffff",font=('Segoe UI',7))

        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        style.configure("Vertical.Scrollbar", background="#FFFFFF", bordercolor="#FFFFFF", arrowcolor="#4D47C3")
        # Add a Treeview widget
                #-------------------------------------------------------------Tree Trip----------------------------------------------------------------
        treeTrip = ttk.Treeview(window, column=( "trip_id","route_id", "driver_id","driver_name","pickup_time","available_seats","trip_status","trip_fee"), show='headings', height=10)
        treeTrip.tag_configure('cell1', background='#ededf9')
        treeTrip.tag_configure('cell2', background='#dbdaf3')
        # "driver_name",
        # "pickup_time",
        # "available_seats",
        # "trip_fee"
        treeTrip.column("trip_id", anchor = CENTER, minwidth=0, width=80,stretch=NO)
        treeTrip.heading("trip_id", text="Trip ID",)

        treeTrip.column("route_id", anchor = CENTER, minwidth=50, width=70,stretch=NO)
        treeTrip.heading("route_id", text="Route ID",)
        treeTrip.column("driver_id", anchor = CENTER, minwidth=50, width=70,stretch=NO)
        treeTrip.heading("driver_id", text="Driver ID",)

        treeTrip.column("driver_name", anchor = CENTER, minwidth=0, width=109,stretch=NO)
        treeTrip.heading("driver_name", text="Driver Name",)

        treeTrip.column("pickup_time", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeTrip.heading("pickup_time", text="Pickup Time",)

        treeTrip.column("available_seats", anchor = CENTER, minwidth=50, width=90,stretch=NO)
        treeTrip.heading("available_seats", text="Available Seats",)

        treeTrip.column("trip_status", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeTrip.heading("trip_status", text="Trip Status",)

        treeTrip.column("trip_fee", anchor = CENTER, minwidth=0, width=80,stretch=NO)
        treeTrip.heading("trip_fee", text="Trip Fee",)

        # "pickup_time",
        # "available_seats",
        # "trip_fee"
        
        getTrips(treeTrip)   #fetching the data

        treeTrip.place(x=170-165+20,y=50-20-5,width=700,height=300-20)
        scrollTrip = ttk.Scrollbar(window, orient="vertical", command=treeTrip.yview)
        scrollTrip.place(x=868-165+20, y=50-20-5, height=285+15-20)

        treeTrip.configure(yscrollcommand=scrollTrip.set)
                #-------------------------------------------------------------Tree Short Route----------------------------------------------------------------
        treeRoute = ttk.Treeview(window, column=( "route_id","route_status"), show='headings', height=10)
        treeRoute.tag_configure('cell1', background='#ededf9')
        treeRoute.tag_configure('cell2', background='#dbdaf3')
        
        treeRoute.column("route_id", anchor = CENTER, minwidth=0, width=75,stretch=NO)
        treeRoute.heading("route_id", text="Route ID",)

        treeRoute.column("route_status", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeRoute.heading("route_status", text="Route status",)
        
        getRoutes(treeRoute)
        treeRoute.place(x=170-165+20,y=300+15,width=175,height=50+20)
        
        #---------------------------------------------------------------
        #---------------------------------------------------------------
        #---------------------------------------------------------------Driver Commuter Treeview------------------------------------------------------
        treeDriverBus = ttk.Treeview(window, column=( "driver_id","commuter_bus_id", "driver_name","telephone_number","gender","national_id","driver_license_expiry","license_plate","bus_license_expiry"), show='headings', height=10)
        treeDriverBus.tag_configure('cell1', background='#ededf9')
        treeDriverBus.tag_configure('cell2', background='#dbdaf3')
        # "driver_id",
        # "commuter_bus_id",
        # "driver_name",
        # "telephone_number",
        # "driver_license_expiry",
        # "license_plate",
        # "bus_license_expiry"
        treeDriverBus.column("driver_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeDriverBus.heading("driver_id", text="Driver ID",)

        treeDriverBus.column("commuter_bus_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeDriverBus.heading("commuter_bus_id", text="Commuter Bus ID",)

        treeDriverBus.column("driver_name", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeDriverBus.heading("driver_name", text="Driver Name",)

        treeDriverBus.column("telephone_number", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeDriverBus.heading("telephone_number", text="Telephone No.",)

        treeDriverBus.column("gender", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeDriverBus.heading("gender", text="Gender",)
        
        treeDriverBus.column("national_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeDriverBus.heading("national_id", text="National ID",)
        
        treeDriverBus.column("driver_license_expiry", anchor = CENTER, minwidth=0, width=150,stretch=NO)
        treeDriverBus.heading("driver_license_expiry", text="Driver License Expiry Date",)

        treeDriverBus.column("license_plate", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeDriverBus.heading("license_plate", text="License Plate",)

        treeDriverBus.column("bus_license_expiry", anchor = CENTER, minwidth=0, width=150,stretch=NO)
        treeDriverBus.heading("bus_license_expiry", text="Bus License Expiry Date",)

        treeDriverBus.place(x=170-165+20,y=50+290+30-20+35+20,width=795+60+100+40,height=300-20)
        scrollDriverBus = ttk.Scrollbar(window, orient="vertical", command=treeDriverBus.yview)
        scrollDriverBus.place(x=868-165+95+20+200, y=50+290+30-20+35+20, height=285+15-20)

        treeDriverBus.configure(yscrollcommand=scrollDriverBus.set)
        getDrivers(treeDriverBus)
        #------------------------------------------------------------------Clients Tree View-------------------------------------------------------------------
        treeClient = ttk.Treeview(window, column=( "client_id","client_name","telephone_number","email","gender"), show='headings', height=10)
        treeClient.tag_configure('cell1', background='#ededf9')
        treeClient.tag_configure('cell2', background='#dbdaf3')

        treeClient.column("client_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeClient.heading("client_id", text="Client ID",)
        treeClient.column("client_name", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeClient.heading("client_name", text="Client Name",)
        treeClient.column("telephone_number", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeClient.heading("telephone_number", text="Telephone No.",)
        treeClient.column("email", anchor = CENTER, minwidth=0, width=150,stretch=NO)
        treeClient.heading("email", text="Email",)
        treeClient.column("gender", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeClient.heading("gender", text="Gender",)
        
        getClients(treeClient)
        treeClient.place(x=170-165+20+600+137+10+10,y=50-20-5+70,width=500+50,height=300-20)
        scrollClient = ttk.Scrollbar(window, orient="vertical", command=treeClient.yview)
        scrollClient.place(x=868-165+20+600-14+10+10, y=50-20-5+70, height=285+15-20)

        treeClient.configure(yscrollcommand=scrollClient.set)
        
        window.mainloop()
        
