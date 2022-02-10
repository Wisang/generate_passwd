from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    f = open('data.txt', "a")
    f.writelines(get_entry_value() + "\n")


def get_entry_value():
    user_data = f"{web_addr_entry.get()} | {mail_entry.get()} \
    | {pass_entry.get()}"
    return user_data
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
                         fg="black")
generate_button.grid(column=2, row=3)

test_label = Label(text="start", bg="white", fg="black")
test_label.grid(row=5, column=1)


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
