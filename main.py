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


    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_ent.delete(0,END)
    password_ent.insert(0, password)

    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_ent.get()
    email_or_username = email_ent.get()
    password = password_ent.get()


    if len(website) == 0 or len(email_or_username) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please Fill out all the boxes")

    else:
        ask = messagebox.askyesno("Yes/no","Are you sure you want save this")
        if ask:
            with open(file = "data.txt", mode= "a") as data:
                data.write(f"Website: {website} | Email/Username: {email_or_username} | Password: {password}\n")

            website_ent.delete(0,END)
            password_ent.delete(0,END)

            messagebox.showinfo("Success", "Details Successfully saved")
# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
# root.minsize(700,400)
root.config(pady=30, padx=30)

logo = PhotoImage(file="logo.png")
canvas = Canvas(root, width=200, height=200, highlightthickness=0)
canvas.create_image(100,100 ,image = logo)
canvas.pack()

frame = Frame(root )
frame.pack()

website_lbl = Label(frame, text="Website", font=("Arial", 20))
website_lbl.grid(row = 0, column= 0)
website_lbl.focus_set()

website_ent = Entry(frame, font=("Arial", 20), width=35)
website_ent.grid(row = 0, column= 1, columnspan = 2)
website_ent.focus_set()

Email_lbl = Label(frame, text="Email/Username", font=("Arial", 20))
Email_lbl.grid(row = 1, column= 0)


email_ent = Entry(frame, font=("Arial", 20),  width=35)
email_ent.grid(row = 1, column= 1, columnspan = 2)
email_ent.insert(0,"EXAMPLE@gmail.com")

password_lbl = Label(frame, text="Password", font=("Arial", 20))
password_lbl.grid(row = 2, column= 0)

password_ent = Entry(frame, font=("Arial", 20), width=22)
password_ent.grid(row = 2, column= 1)

generate_password_button = Button(frame, text= "Generate Password", command= generate_password)
generate_password_button.grid(row=2, column = 2, ipady = 4)

add_password_button = Button(frame, text="Add", width=44, command=save_data)
add_password_button.grid(row = 3, column = 1, columnspan = 2, ipady = 4)



root.mainloop()