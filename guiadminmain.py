from tkinter import *
from tkinter import ttk, Button, Label,font
from adminmain import *

   
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
        
        # x=868-165+95+20, y=50+290+30-20,
        canvas.create_rectangle(0, 384-45, 1448, 385-45, fill="#d3d3d3", outline = '#d3d3d3')
        
        canvas.create_text(541.0+300+75+80+30+30+70,181.0+185+40-30,anchor="nw",text="Driver and Commuter Bus",fill="#4D47C3",font=("Segoe UI", 10,'bold'))
        mainEntryLabelFont= font.Font(family='Segoe UI', size=8, weight='bold')
        mainEntryFont= font.Font(family='Segoe UI', size=8)
        
        canvas.create_text(541.0+300+75+80+30+30,181.0+185+40,anchor="nw",text="First Name",fill="#4D47C3",font=mainEntryLabelFont)
        first_name_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        first_name_entry.place(x=539.0+300+75+80+30+30,y=202.0+185+40,width=130.0,height=20.0)
        
        canvas.create_text(541.0+300+75+80+30+30,181.0+185+50+40,anchor="nw",text="Last Name",fill="#4D47C3",font=mainEntryLabelFont)
        last_name_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        last_name_entry.place(x=539.0+300+75+80+30+30,y=202.0+185+50+40,width=130.0,height=20.0)
        
        canvas.create_text(541.0+300+75+80+30+30,181.0+185+50+50+40,anchor="nw",text="Telephone No.",fill="#4D47C3",font=mainEntryLabelFont)
        telephone_number_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        telephone_number_entry.place(x=539.0+300+75+80+30+30,y=202.0+185+50+50+40,width=130.0,height=20.0)
        
        canvas.create_text(541.0+300+75+80+30+30,181.0+185+50+50+50+40,anchor="nw",text="Gender",fill="#4D47C3",font=mainEntryLabelFont)
        gender_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        gender_entry.place(x=539.0+300+75+80+30+30,y=202.0+185+50+50+50+40,width=130.0,height=20.0)
        #---------------------------------------------------------------
        canvas.create_text(541.0+300+190+75+80+30,181.0+185+40,anchor="nw",text="National ID",fill="#4D47C3",font=mainEntryLabelFont)
        national_id_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        national_id_entry.place(x=539.0+300+190+75+80+30,y=202.0+185+40,width=130.0,height=20.0)
        
        
        def dateEntryFocusOut(Entry):
            if len(Entry.get())==0:
                Entry.insert('0',"YYYY-MM-DD")
        def dateEntryFocusIn(Entry):
            if Entry.get()=="YYYY-MM-DD":
                Entry.delete('0','end')
        
        canvas.create_text(541.0+300+190+75+80+30,181.0+185+50+40,anchor="nw",text="Driver License Exp. Date",fill="#4D47C3",font=mainEntryLabelFont)
        driver_license_expiry_date_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        driver_license_expiry_date_entry.place(x=539.0+300+190+75+80+30,y=202.0+185+50+40,width=130.0,height=20.0)
        driver_license_expiry_date_entry.insert(0,"YYYY-MM-DD")
        driver_license_expiry_date_entry.bind("<FocusIn>", lambda args: dateEntryFocusIn(driver_license_expiry_date_entry))
        driver_license_expiry_date_entry.bind("<FocusOut>", lambda args: dateEntryFocusOut(driver_license_expiry_date_entry))
        
        
        canvas.create_text(541.0+300+190+75+80+30,181.0+185+50+50+40,anchor="nw",text="License Plate",fill="#4D47C3",font=mainEntryLabelFont)
        license_plate_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        license_plate_entry.place(x=539.0+300+190+75+80+30,y=202.0+185+50+50+40,width=130.0,height=20.0)
        
        
        
                
        canvas.create_text(541.0+300+190+75+80+30,181.0+185+50+50+50+40,anchor="nw",text="Bus License Exp. Date",fill="#4D47C3",font=mainEntryLabelFont)
        bus_license_expiry_date_entry = Entry(bd=0,font=mainEntryFont,bg="#d3d3d3",highlightthickness=0)
        bus_license_expiry_date_entry.place(x=539.0+300+190+75+80+30,y=202.0+185+50+50+50+40,width=130.0,height=20.0)
        bus_license_expiry_date_entry.insert(0,"YYYY-MM-DD")
        bus_license_expiry_date_entry.bind("<FocusIn>", lambda args: dateEntryFocusIn(bus_license_expiry_date_entry))
        bus_license_expiry_date_entry.bind("<FocusOut>", lambda args: dateEntryFocusOut(bus_license_expiry_date_entry))
        
        
        
        
        mainButtonFont= font.Font(family='Segoe UI', size=7, weight='bold')
        
        add_driver_bus_button = Button(text='Add',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:addDriver(treeDriverBus,first_name_entry,last_name_entry,telephone_number_entry,gender_entry,national_id_entry,driver_license_expiry_date_entry,license_plate_entry,bus_license_expiry_date_entry) ,
                               relief="flat"
                        )

        add_driver_bus_button.place(x=531.0+400+60+80,y=555.0+20+40,width=109.0-30,height=32.0)

        update_driver_bus_button = Button(text='Update',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:updateDriver(treeDriverBus,first_name_entry,last_name_entry,telephone_number_entry,gender_entry,national_id_entry,driver_license_expiry_date_entry,license_plate_entry,bus_license_expiry_date_entry),
                               relief="flat"
                        )

        update_driver_bus_button.place(x=531.0+488+60+80,y=555.0+20+40,width=109.0-30,height=32.0)      
        
        delete_driver_bus_button = Button(text='Delete',bg='#4D47C3',fg='#ffffff',font=mainButtonFont, borderwidth=0,highlightthickness=0,
                               command=lambda:deleteDriver(treeDriverBus),
                               relief="flat"
                        )

        delete_driver_bus_button.place(x=531.0+488+60+80+88,y=555.0+20+40,width=109.0-30,height=32.0)  
        
        
        #-------------------------------------------------------------            
        style = ttk.Style()

        # style.theme_use('clam')
        style.configure('Treeview.Heading', background="#ffffff",foreground="#4D47C3",font=('Segoe UI',8,'bold'))
        style.configure('Treeview', background="#ffffff",font=('Segoe UI',7))

        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        style.configure("Vertical.Scrollbar", background="#FFFFFF", bordercolor="#FFFFFF", arrowcolor="#4D47C3")
        # Add a Treeview widget

        treeTrip = ttk.Treeview(window, column=( "trip_id","route_id", "driver_name","pickup_time","available_seats","trip_status","trip_fee"), show='headings', height=10)
        treeTrip.tag_configure('cell1', background='#ededf9')
        treeTrip.tag_configure('cell2', background='#dbdaf3')
        # "driver_name",
        # "pickup_time",
        # "available_seats",
        # "trip_fee"
        treeTrip.column("trip_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeTrip.heading("trip_id", text="Trip ID",)

        treeTrip.column("route_id", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeTrip.heading("route_id", text="Route ID",)

        treeTrip.column("driver_name", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeTrip.heading("driver_name", text="Driver Name",)

        treeTrip.column("pickup_time", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeTrip.heading("pickup_time", text="Pickup Time",)

        treeTrip.column("available_seats", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeTrip.heading("available_seats", text="Available Seats",)

        treeTrip.column("trip_status", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeTrip.heading("trip_status", text="Trip Status",)

        treeTrip.column("trip_fee", anchor = CENTER, minwidth=0, width=100,stretch=NO)
        treeTrip.heading("trip_fee", text="Trip Fee",)

        # "pickup_time",
        # "available_seats",
        # "trip_fee"
        
        getTrips(treeTrip)   #fetching the data

        treeTrip.place(x=170-165+20,y=50-20,width=700,height=300)
        scrollTrip = ttk.Scrollbar(window, orient="vertical", command=treeTrip.yview)
        scrollTrip.place(x=868-165+20, y=50-20, height=285+15)

        treeTrip.configure(yscrollcommand=scrollTrip.set)

        #---------------------------------------------------------------
        #---------------------------------------------------------------
        #---------------------------------------------------------------
        #---------------------------------------------------------------
        #---------------------------------------------------------------
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

        treeDriverBus.place(x=170-165+20,y=50+290+30-20,width=795+60+100+40,height=300)
        scrollDriverBus = ttk.Scrollbar(window, orient="vertical", command=treeDriverBus.yview)
        scrollDriverBus.place(x=868-165+95+20+200, y=50+290+30-20, height=285+15)

        treeDriverBus.configure(yscrollcommand=scrollDriverBus.set)
        getDrivers(treeDriverBus)

        window.mainloop()
