from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH ------------------------------- #
def search_website():
    if len(website_entry.get()) > 0:
        try:
            with open("data.json", "r") as file:
                json_query = json.load(file)
                try:
                    web_data = json_query[website_entry.get()]
                    messagebox.showinfo(title=website_entry.get(),
                                        message=f"Email: {web_data['email']}\n Password: {web_data['password']}")
                except KeyError:
                    messagebox.showinfo(title=website_entry.get(), message="Website not found")
                else:
                    messagebox.showinfo(title=website_entry.get(), message="Website not found")
        except FileNotFoundError:
            messagebox.showinfo(title=website_entry.get(), message="First time use try again")
    else:
        messagebox.showwarning(title="Search", message="No website selected")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for n in range(nr_letters)]

    password_list += [random.choice(symbols) for n in range(nr_symbols)]

    password_list += [random.choice(numbers) for n in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Oops', message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="website",
                                       message=f"these are the details entered\n Email: {email}\nPassword: {password}\n Is it okay to save ?")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # read old data
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pass")
window.config(padx=50, pady=50)
#
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, pady=2)
website_entry.focus()
email_entry = Entry()
email_entry.insert(0, "long@man.com")
email_entry.grid(column=1, row=2, pady=2)
password_entry = Entry()
password_entry.grid(column=1, row=3, pady=2)

# button
search_btn = Button(text="search", command=search_website)
search_btn.grid(column=2, row=1)
gen_pass_btn = Button(text="Generate Password", command=generate_password)
gen_pass_btn.grid(column=2, row=3)
add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, pady=2)

window.mainloop()
