from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ------------------------------ SEARCH WEBSITE --------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        if website in data:
            saved_email = data[website]["email"]
            saved_password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {saved_email}\npassword: {saved_password}")
        else:
            messagebox.showinfo(title=website, message=f"No data for {website} found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for item in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for item in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for item in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email_ = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email_,
                          "password": password
                          }
                }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Empty field", message=f"please fill all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Email: {email_}\nPassword: {password}\nDo you want to save?")

        if is_ok:
            try:
                with open("passwords.json", "r") as data_file:
                    #reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("passwords.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #updating old data
                data.update(new_data)

                with open("passwords.json", "w") as data_file:
                    #saving updated data into file
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

###
canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
###
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, )
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")  # 0 IS THE INDEX WHERE WE ARE INSERTING THE STRING

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=add)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

window.mainloop()

add_button = Button(text="Add", width=44, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
