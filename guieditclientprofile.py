from tkinter import Tk, Canvas, Entry, Button, font
from re import *
from viewprofile import * 
from editprofile import * 

class EditClientProfilePage:
    def __init__(self,id):
        client_id_passed=id
        cursor=displayClientProfile(client_id_passed)
        clientData=cursor.fetchone()

        window = Tk()
        window.title("Waddy Edit Client Profile")
        window.geometry("1048x768")
        window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 768,
            width = 1048,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            70.0,
            89.0,
            anchor="nw",
            text=clientData[0]+" "+clientData[1],
            fill="#000000",
            font=("Segoe UI", 50 * -1)
        )

        canvas.create_text(
            70.0,
            203.0,
            anchor="nw",
            text="First Name",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            220.0,
            203.0,
            anchor="nw",
            text=clientData[0],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        firstname_entry = Entry(
            bd=0,
            bg="#EFEFFF",
            highlightthickness=0
        )
        firstname_entry.place(
            x=580.0,
            y=203.0,
            width=393.0,
            height=41.0
        )

        canvas.create_text(
            70.0,
            262.0,
            anchor="nw",
            text="Last Name",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            220.0,
            262.0,
            anchor="nw",
            text=clientData[1],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        lastname_entry = Entry(
            bd=0,
            bg="#EFEFFF",
            highlightthickness=0
        )
        lastname_entry.place(
            x=580.0,
            y=262.0,
            width=393.0,
            height=41.0
        )

        canvas.create_text(
            70.0,
            320.0,
            anchor="nw",
            text="Email",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            220.0,
            320.0,
            anchor="nw",
            text=clientData[4],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        email_entry = Entry(
            bd=0,
            bg="#EFEFFF",
            highlightthickness=0
        )
        email_entry.place(
            x=580.0,
            y=320.0,
            width=393.0,
            height=41.0
        )

        canvas.create_text(
            70.0,
            380.0,
            anchor="nw",
            text="Password",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            220.0,
            380.0,
            anchor="nw",
            text=clientData[5],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        password_entry = Entry(
            bd=0,
            bg="#EFEFFF",
            highlightthickness=0
        )
        password_entry.place(
            x=580.0,
            y=380.0,
            width=393.0,
            height=41.0
        )

        canvas.create_text(
            70.0,
            443.0,
            anchor="nw",
            text="ID",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            220.0,
            443.0,
            anchor="nw",
            text=client_id_passed,
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            70.0,
            505.0,
            anchor="nw",
            text="Gender",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            220.0,
            505.0,
            anchor="nw",
            text=clientData[3],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )
        
        gender_entry = Entry(
            bd=0,
            bg="#EFEFFF",
            highlightthickness=0
        )
        gender_entry.place(
            x=580.0,
            y=505.0,
            width=393.0,
            height=41.0
        )
    

        canvas.create_text(
            70.0,
            567.0,
            anchor="nw",
            text="Phone no.",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            220.0,
            567.0,
            anchor="nw",
            text=clientData[2],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        phone_entry = Entry(
            bd=0,
            bg="#EFEFFF",
            highlightthickness=0
        )
        phone_entry.place(
            x=580.0,
            y=567.0,
            width=393.0,
            height=41.0
        )
        
        def redirectToMainpage():
            window.destroy()
            import guiclientmain
            guiclientmain.ClientMainPage(client_id_passed)

        buttonFont = font.Font(family='Segoe UI', size=18, weight='bold')

        save_profile_button = Button(text='Save changes',
                                    bg='#4D47C3',
                                    fg='#ffffff',
                                    font=buttonFont,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: [SaveClient(firstname_entry,lastname_entry,email_entry,phone_entry,gender_entry,client_id_passed,password_entry),redirectToMainpage()],
                                    relief="flat"
                        )

        save_profile_button.place(x=807.0,y=104.0,width=167.0,height=70.0)

        buttonFont = font.Font(family='Segoe UI', size=14, weight='bold')
        go_back_button = Button(text='Go back to main page',bg='#ffffff',fg='#4D47C3',font=buttonFont,borderwidth=0,highlightthickness=0,
                               command=lambda:redirectToMainpage(),
                               relief="flat"
                        )

        go_back_button.place(x=65.0,y=611,width=200.0,height=42.0)

        window.resizable(False, False)
        window.mainloop()
