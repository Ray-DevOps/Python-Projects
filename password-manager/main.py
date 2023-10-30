from tkinter import *               # The * only imports all classes but doesn't import messagebox which is a separate module
from tkinter import messagebox     # We therefore have to import this separately for use in our program
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for cha in range(randint(2, 4))]
    password_numbers = [choice(numbers) for ch in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)        # the pyperclip copy method allows us to copy text to clipboard.
                                    # there is also the pyperclip paste method which allows us to paste to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=400)


canvas = Canvas(width=500, height=400, bg="grey", highlightthickness=0)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(250, 150, image=padlock_img)
canvas.create_text(90, 260, text="Website:", font=("Arial", 11, "bold"))
canvas.create_text(90, 295, text="Email/Username:", font=("Arial", 11, "bold"))
canvas.create_text(90, 330, text="Password:", font=("Arial", 11, "bold"))
canvas.pack()
def data_gathered():
    site = website_input.get()
    user = username_input.get()
    pswd = password_input.get()
    pswd_dict = {
        site: {
            "username": user,
            "password": pswd,
        }
    }

    if len(site) != 0 and len(user) != 0 and len(pswd) != 0:
        is_ok = messagebox.askokcancel(title=site,
                                       message=f"These are the details entered: \nUsername: {user} \nPassword: {pswd} \nClick 'OK' to save or 'Cancel' to cancel")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(pswd_dict, data_file, indent=4)
            else:
                data.update(pswd_dict)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                username_input.delete(0, END)
                password_input.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

def find_password():
    site = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data file found")
    else:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

        if site in list(data.keys()):
            username = data[site]["username"]
            password = data[site]["password"]
            messagebox.showinfo(title=f"Find below details for {site}",
                                message=f"username: {username}\npassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No data found for {site}")

website_input = Entry(width=15, font=("Arial", 15))
website_input.focus()   # This allows the cursor to be automatically inside this field when the program is launched
website_input.place(x=160, y=245)
username_input = Entry(width=28, font=("Arial", 15))
username_input.place(x=160, y=280)
username_input.insert(0, "anyaraymond@yahoo.com") # The insert method allows you to enter a default (prepopulated) value for username when the program launches
password_input = Entry(width=15, font=("Arial", 15))
password_input.place(x=160, y=315)

generate_button = Button(text="Generate Password", command=generate_password, font=("Arial", 10, "bold"))
generate_button.place(x=340, y=316)
add_button = Button(text="Add", width=38, command=data_gathered, font=("Arial", 10, "bold"))
add_button.place(x=160, y=350)
search_button = Button(text="Search", command=find_password, font=("Arial", 10, "bold"), width=16)
search_button.place(x=340, y=245)

window.mainloop()




