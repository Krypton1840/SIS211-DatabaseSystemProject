from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Radiobutton, Toplevel, messagebox,Frame
from re import *
from signup import * 
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Waddy SignUp")
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


canvas.create_text(52.0,42.0,anchor="nw",text="Waddy",fill="#000000",font=("Segoe UI", 20 * -1))

canvas.create_text(129.0,284.0,anchor="nw",text="Sign Up to ",fill="#000000",font=("Segoe UI", 50 * -1, 'bold'))

canvas.create_text(129.0,354.0,anchor="nw",text="Waddy",fill="#000000",font=("Segoe UI", 35 * -1))

canvas.create_text(133.0,446.0,anchor="nw",text="If you already have an account ",fill="#000000",font=("Segoe UI", 16 * -1))

canvas.create_text(133.0,472.0,anchor="nw",text="You can Login here !",fill="#000000",font=("Segoe UI", 16 * -1))



#-----------------------------------------First Name [ Entry ]-----------------------------------------

canvas.create_text(541.0,181.0,anchor="nw",text="First Name",fill="#A7A2FF",font=("Segoe UI", 15 * -1))

first_name_entry_image = PhotoImage( file=relative_to_assets("first_name_entry_image.png"))

first_name_entry_bg = canvas.create_image(735.5,223.5,image=first_name_entry_image)

first_name_entry = Entry(bd=0,bg="#EFEFFF",highlightthickness=0)

first_name_entry.place(x=539.0,y=202.0,width=393.0,height=41.0)

#-----------------------------------------Last Name [ Entry ]-----------------------------------------

canvas.create_text(541.0,249.0,anchor="nw",text="Last Name",fill="#A7A2FF",font=("Segoe UI", 15 * -1))

last_name_entry_image = PhotoImage(file=relative_to_assets("last_name_entry_image.png"))

last_name_entry_bg = canvas.create_image(735.5,292.0,image=last_name_entry_image)

last_name_entry = Entry(bd=0,bg="#EFEFFF",highlightthickness=0)

last_name_entry.place(x=539.0,y=270.0,width=393.0,height=42.0)

#-----------------------------------------Email [ Entry ]-----------------------------------------

canvas.create_text(541.0,317.0,anchor="nw",text="Email",fill="#A7A2FF",font=("Segoe UI", 15 * -1))

email_entry_image = PhotoImage(file=relative_to_assets("email_entry_image.png"))

email_entry_bg = canvas.create_image(735.5,359.0,image=email_entry_image)

email_entry = Entry(bd=0,bg="#EFEFFF",highlightthickness=0)

email_entry.place(x=539.0,y=337.0,width=393.0,height=42.0)

#-----------------------------------------Password [ Entry ]-----------------------------------------

canvas.create_text(541.0,385.0,anchor="nw",text="Password",fill="#A7A2FF",font=("Segoe UI", 15 * -1))

password_entry_image = PhotoImage(file=relative_to_assets("password_entry_image.png"))

password_entry_bg = canvas.create_image(735.5,427.5,image=password_entry_image)

password_entry = Entry(bd=0,show="●",bg="#EFEFFF",highlightthickness=0)

password_entry.place(x=539.0,y=406.0,width=393.0,height=41.0)

#-----------------------------------------Telephone Number [ Entry ]-----------------------------------------

canvas.create_text(541.0,453.0,anchor="nw",text="Telephone Number",fill="#A7A2FF",font=("Segoe UI", 15 * -1))

telephone_entry_image = PhotoImage(file=relative_to_assets("telephone_entry_image.png"))

telephone_entry_bg = canvas.create_image(735.5,495.5,image=telephone_entry_image)

telephone_entry = Entry(bd=0,bg="#EFEFFF",highlightthickness=0)

telephone_entry.place(x=539.0,y=473.0,width=393.0,height=43.0)


#-----------------------------------------SignUp [ Button ]-----------------------------------------

signup_button_image = PhotoImage(file=relative_to_assets("signup_button_image.png"))

signup_button = Button(image=signup_button_image,borderwidth=0,highlightthickness=0,
                       command=lambda:[signUp(first_name_entry,last_name_entry,email_entry,password_entry,telephone_entry)],
                       relief="flat"
                )

signup_button.place(x=531.0,y=555.0,width=409.0,height=42.0)




window.resizable(False, False)
window.mainloop()
