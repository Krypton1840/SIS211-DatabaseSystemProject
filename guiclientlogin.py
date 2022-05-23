from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Radiobutton, Toplevel, messagebox,Frame,font
from login import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ClientLoginPage:
    def __init__(self):
            
        window = Tk()
        window.title("Waddy Client Log In")
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

        # First TextBox for email
        canvas.create_text(
            890.0-349,
            290.0,
            anchor="nw",
            text="Email",
            fill="#A7A2FF",
            font=("Segoe UI Regular", 15 * -1)
        )

        # email_entry_image = PhotoImage(
        #     file=relative_to_assets("userid_entry_image.png"))
        # email_entry_bg = canvas.create_image(
        #     898.0-349,
        #     313.0,
        #     image=email_entry_image
        # )
        email_entry = Entry(
            bd=0,
            bg="#EFEFFF",
            highlightthickness=0
        )
        email_entry.place(
            x=898.0-358,
            y=313.0,
            width=393.0,
            height=41.0
        )

        # Second TextBox for password
        canvas.create_text(
            890.0-349,
            388.0,
            anchor="nw",
            text="Password",
            fill="#A7A2FF",
            font=("Segoe UI Regular", 15 * -1)
        )

        # password_entry_image = PhotoImage(
        #     file=relative_to_assets("password_entry_image.png"))
        # password_entry_bg = canvas.create_image(
        #     1094.5,
        #     432.5,
        #     image=password_entry_image
        # )

        password_entry = Entry(
            bd=0,
            show="●",
            bg="#EFEFFF",
            highlightthickness=0
        )

        password_entry.place(
            x=890.0-349,
            y=411.0,
            width=393.0,
            height=41.0
        )

        canvas.create_text(
            175.0,
            294.0,
            anchor="nw",
            text="Log in to ",
            fill="#000000",
            font=("Segoe UI", 50 * -1, 'bold')
        )

        canvas.create_text(
            175.0,
            374.0,
            anchor="nw",
            text="Waddy",
            fill="#000000",
            font=("Segoe UI Medium", 35 * -1)
        )

        # Log in button
        # log_in_button_image = PhotoImage(
        #     file=relative_to_assets("log_in_button_image.png"))
        # log_in_button = Button(
        #     image=log_in_button_image,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: attemptClientLogIn(email_entry,password_entry),
        #     relief="flat"
        # )
        buttonFont = font.Font(family='Segoe UI', size=18, weight='bold')
        log_in_button = Button(
            text='Log in',bg='#4D47C3',fg='#ffffff',font=buttonFont,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: attemptClientLogIn(email_entry,password_entry),
            relief="flat"
        )
        log_in_button.place(
            x=890.0-358,
            y=494.0,
            width=409.0,
            height=40.0
        )

        # Function to go back to main menu
        def goBackToMenu():
            window.destroy()
            import gui
            gui.MenuPage()
        
        # Button to use the goBackToMenu() function
        buttonFont = font.Font(family='Segoe UI', size=14, weight='bold')
        go_back_button = Button(text='Go back to menu',bg='#ffffff',fg='#4D47C3',font=buttonFont,borderwidth=0,highlightthickness=0,
                               command=goBackToMenu,
                               relief="flat"
                        )

        go_back_button.place(x=89.0,y=611,width=160.0,height=42.0)

        window.resizable(False, False)
        window.mainloop()