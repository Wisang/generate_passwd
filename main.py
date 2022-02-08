from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from turtle import width

window = Tk()
window.config(bg="white", padx=20, pady=20)
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
                         fg="black")
generate_button.grid(column=2, row=3)

generate_button = Button(text="Add", width=36, bg="white",
                         fg="black")
generate_button.grid(row=4, column=1, columnspan=2)

web_addr = Entry(width=35, bg="white", fg="black")
web_addr.grid(row=1, column=1, columnspan=2)

mail_entry = Entry(width=35, bg="white", fg="black")
mail_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=24, bg="white", fg="black")
pass_entry.grid(row=3, column=1)






window.mainloop()
