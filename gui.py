from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Radiobutton, Toplevel, messagebox,Frame,font
from re import *
from signup import * 
from login import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MenuPage:
    def __init__(self):
        
        window = Tk()
        window.title("Waddy Menu")
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

        def goClientSignUp():
            window.destroy()
            import guiclientsignup
            guiclientsignup.ClientSignUpPage()
        def goAdminSignUp():
            window.destroy()
            import guiadminsignup
            guiadminsignup.AdminSignUpPage()
        def goClientLogin():
            window.destroy()
            import guiclientlogin
            guiclientlogin.ClientLoginPage()
        def goAdminLogin():
            window.destroy()
            import guiadminlogin
            guiadminlogin.AdminLoginPage()

        #-----------------------------------------Choose [ Button ]-----------------------------------------

        buttonFont = font.Font(family='Segoe UI', size=18, weight='bold')

        signup_client_button = Button(text='Sign up client',bg='#4D47C3',fg='#ffffff',font=buttonFont,borderwidth=0,highlightthickness=0,
                               command=goClientSignUp,
                               relief="flat"
                        )

        signup_client_button.place(x=319.0,y=384.0,width=409.0,height=42.0)

        signup_admin_button = Button(text='Sign up admin',bg='#4D47C3',fg='#ffffff',font=buttonFont,borderwidth=0,highlightthickness=0,
                               command=goAdminSignUp,
                               relief="flat"
                        )

        signup_admin_button.place(x=319.0,y=300.0,width=409.0,height=42.0)
        login_client_button = Button(text='Login client',bg='#4D47C3',fg='#ffffff',font=buttonFont,borderwidth=0,highlightthickness=0,
                               command=goClientLogin,
                               relief="flat"
                        )

        login_client_button.place(x=319.0,y=384.0,width=409.0,height=42.0)

        login_admin_button = Button(text='Login Admin',bg='#4D47C3',fg='#ffffff',font=buttonFont,borderwidth=0,highlightthickness=0,
                               command=goAdminLogin,
                               relief="flat"
                        )

        login_admin_button.place(x=319.0,y=300.0,width=409.0,height=42.0)


        window.resizable(False, False)
        window.mainloop()

if __name__ == "__main__":
    app = MenuPage()
    #app.mainloop()