from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = web_addr_entry.get()
    email = mail_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="empty")
    else:
        is_ok = messagebox.askokcancel(title="website", message='ok to save?')

        if is_ok:
            with open('data.txt', "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_addr_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(bg="white", padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white", fg="black")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:", bg="white", fg="black")
user_label.grid(row=2, column=0)

pass_label = Label(text="Password", bg="white", fg="black")
pass_label.grid(row=3, column=0)

generate_button = Button(text="Generate Password", bg="white",
                         fg="black", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, bg="white",
                         fg="black", command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

web_addr_entry = Entry(width=39)
web_addr_entry.grid(row=1, column=1, columnspan=2)
web_addr_entry.focus()

mail_entry = Entry(width=39)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "wseom7@gmail.com")

pass_entry = Entry(width=22)
pass_entry.grid(row=3, column=1)



window.mainloop()
