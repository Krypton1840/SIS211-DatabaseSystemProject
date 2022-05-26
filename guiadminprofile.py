from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Radiobutton, Toplevel, messagebox,Frame,font
from re import *
from profile import * 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ViewAdminProfilePage:
    def __init__(self):
        admin_id_passed="1110000"
        cursor=displayAdminProfile(admin_id_passed)
        adminData=cursor.fetchone()
        print(adminData)

        window = Tk()
        window.title("Waddy Admin Profile")
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
            147.0,
            89.0,
            anchor="nw",
            text=adminData[0]+" "+adminData[1],
            fill="#000000",
            font=("Segoe UI", 50 * -1)
        )

        buttonFont = font.Font(family='Segoe UI', size=18, weight='bold')

        edit_profile_button = Button(text='Edit',bg='#4D47C3',fg='#ffffff',font=buttonFont,borderwidth=0,highlightthickness=0,
                               relief="flat"
                        )

        edit_profile_button.place(x=708.0,y=104.0,width=147.0,height=70.0)

        canvas.create_text(
            147.0,
            545.0,
            anchor="nw",
            text="National ID",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            347.0,
            545.0,
            anchor="nw",
            text=adminData[2],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )
        
        canvas.create_text(
            
            147.0,
            466.0,
            anchor="nw",
            text="Gender",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )
        
        canvas.create_text(
            347.0,
            466.0,
            anchor="nw",
            text=adminData[4],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            147.0,
            301.0,
            anchor="nw",
            text="ID",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            347.0,
            301.0,
            anchor="nw",
            text=admin_id_passed,
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            147.0,
            216.0,
            anchor="nw",
            text="Full Name",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )
        
        canvas.create_text(
            347.0,
            216.0,
            anchor="nw",
            text=adminData[0]+" "+adminData[1],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            147.0,
            383.0,
            anchor="nw",
            text="Phone no.",
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        canvas.create_text(
            347.0,
            383.0,
            anchor="nw",
            text=adminData[3],
            fill="#A7A2FF",
            font=("Segoe UI", 25 * -1)
        )

        #-----------------------------Go Back [Button]------------------------------------
        # def goBackToMenu():
        #     window.destroy()
        #     import gui
        #     gui.MenuPage()
        # buttonFont = font.Font(family='Segoe UI', size=14, weight='bold')
        # go_back_button = Button(text='Go back to menu',bg='#ffffff',fg='#4D47C3',font=buttonFont,borderwidth=0,highlightthickness=0,
        #                        command=goBackToMenu,
        #                        relief="flat"
        #                 )

        # go_back_button.place(x=89.0,y=611,width=160.0,height=42.0)

        
        window.resizable(False, False)
        window.mainloop()

if __name__ == "__main__":
    app = ViewAdminProfilePage()
    #app.mainloop()