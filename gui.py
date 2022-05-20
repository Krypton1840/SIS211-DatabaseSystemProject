from pathlib import Path


from tkinter import *
from login import *
# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Waddy Log In")
window.geometry("1440x900")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 900,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

canvas.create_text(
    890.0,
    290.0,
    anchor="nw",
    text="Enter ID",
    fill="#A7A2FF",
    font=("Segoe UI Regular", 15 * -1)
)

# First TextBox for email or username
userid_entry_image = PhotoImage(
    file=relative_to_assets("userid_entry_image.png"))
userid_entry_bg = canvas.create_image(
    1094.5,
    334.5,
    image=userid_entry_image
)
userid_entry = Entry(
    bd=0,
    bg="#EFEFFF",
    highlightthickness=0
)
userid_entry.place(
    x=898.0,
    y=313.0,
    width=393.0,
    height=41.0
)


canvas.create_text(
    890.0,
    388.0,
    anchor="nw",
    text="Password",
    fill="#A7A2FF",
    font=("Segoe UI Regular", 15 * -1)
)

# Second TextBox
password_entry_image = PhotoImage(
    file=relative_to_assets("password_entry_image.png"))
password_entry_bg = canvas.create_image(
    1094.5,
    432.5,
    image=password_entry_image
)

password_entry = Entry(
    bd=0,
    bg="#EFEFFF",
    highlightthickness=0
)

password_entry.place(
    x=898.0,
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

canvas.create_text(
    179.0,
    480.0,
    anchor="nw",
    text="If you don’t have an account",
    fill="#000000",
    font=("Segoe UI Regular", 16 * -1)
)

canvas.create_text(
    179.0,
    510.0,
    anchor="nw",
    text="You can   Register here !",
    fill="#000000",
    font=("Segoe UI Regular", 16 * -1)
)

# Log in button
log_in_button_image = PhotoImage(
    file=relative_to_assets("log_in_button_image.png"))
log_in_button = Button(
    image=log_in_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: attemptLogIn(userid_entry,password_entry),
    relief="flat"
)

log_in_button.place(
    x=890.0,
    y=494.0,
    width=409.0,
    height=40.0
)

window.resizable(False, False)
window.mainloop()