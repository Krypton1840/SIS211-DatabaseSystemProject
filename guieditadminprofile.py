from tkinter import Tk, Canvas, Entry, Button,font
from re import *
from viewprofile import * 
from editprofile import * 

class EditAdminProfilePage:
    def __init__(self,id):
        admin_id_passed=id
        cursor=displayAdminProfile(admin_id_passed)
        adminData=cursor.fetchone()

        window = Tk()
        window.title("Waddy Edit Admin Profile")
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
            text=adminData[0]+" "+adminData[1],
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
            text=adminData[0],
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
            text=adminData[1],
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
            text="National ID",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            220.0,
            320.0,
            anchor="nw",
            text=adminData[2],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        nationalID_entry = Entry(
            bd=0,
            bg="#EFEFFF",
            highlightthickness=0
        )
        nationalID_entry.place(
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
            text=adminData[5],
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
            text=admin_id_passed,
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
            text=adminData[4],
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
            text=adminData[3],
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
        

        buttonFont = font.Font(family='Segoe UI', size=18, weight='bold')

        def redirectToMainpage():
            window.destroy()
            import guiadminmain
            guiadminmain.AdminMainPage(admin_id_passed)

        save_profile_button = Button(text='Save changes',
                                    bg='#4D47C3',
                                    fg='#ffffff',
                                    font=buttonFont,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: [SaveAdmin(firstname_entry,lastname_entry,nationalID_entry,phone_entry,gender_entry,admin_id_passed,password_entry),redirectToMainpage()],
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

