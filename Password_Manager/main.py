import pyperclip
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox

FONT_NAME = "Roboto"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "P", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = [ "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "=", ":", "?"]
    num_of_letter = randint(8, 10)
    num_of_numbers = randint(2, 4)
    num_of_symbols = randint(2, 4)

    generated_password_list = [choice(letters) for _ in range(num_of_letter)]
    
    generated_password_list.extend([choice(numbers) for _ in range(num_of_numbers)])

    generated_password_list.extend([choice(symbols) for _ in range(num_of_symbols)])

    shuffle(generated_password_list)

    generated_password = "".join(generated_password_list)

    password_input.insert(0, generated_password)

    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email_or_username = user_name_input.get()
    password = password_input.get()


    def add():
        messagebox.askquestion(title=website, message=f"Email: {email_or_username}\nPassword: {password}\nIs this ok?")

    add()
    with open("data.txt", mode="r") as data:
        content = data.readlines()
        with open("data.txt", mode="a") as data:
            if len(content) != 0:
                data.write(f"\n{website} | {email_or_username} | {password}")
            else:
                data.write(f"{website} | {email_or_username} | {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(width=200, height=200)


canva = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canva.create_image(100, 100, image=logo_img)
canva.grid(column=1, row=0)


website_label = Label(text="Website:", font=(FONT_NAME, 10, "normal"))
website_label.grid(column=0, row=1)


website_input = Entry(width=50)
website_input.grid(column=1, row=1, columnspan=2)


user_name_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "normal"))
user_name_label.grid(column=0, row=2)


user_name_input = Entry(width=50)
user_name_input.grid(column=1, row=2, columnspan=2)


password_label = Label(text="Password:", font=(FONT_NAME, 10, "normal"))
password_label.grid(column=0, row=3)


password_input = Entry(width=29)
password_input.grid(column=1, row=3)


generate_pass_button = Button(text="Generate Password", width=15, command=generate_password)
generate_pass_button.grid(column=2, row=3, sticky="e", padx=(0, 13))


add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()