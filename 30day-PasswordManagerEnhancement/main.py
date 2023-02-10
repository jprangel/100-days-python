from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
FILENAME = "password_database.json"

def pass_options():
    """ Check the password lenth option and randomly choose character in the lists"""
    i = 1
    global password
    password = []
    global pass_options_dict
    pass_options_dict = { "letters": check_op_let.get(), "numbers": check_op_num.get(), "symbols": check_op_sym.get() }

    while int(spinbox.get())  > len(password):
        for k in pass_options_dict:
            if pass_options_dict[k] == 1:
                if k == "letters":
                    item = [random.choice(letters) for x in range(i)]
                    password += item
                    if int(spinbox.get())  == len(password):
                        break
                elif k == "symbols":
                    item = [random.choice(symbols) for x in range(i)]
                    password += item
                    if int(spinbox.get())  == len(password):
                        break
                elif k == "numbers":
                    item = [random.choice(numbers) for x in range(i)]
                    password += item
                    if int(spinbox.get())  == len(password):
                        break

def pass_generator():
    """Validate if any options is empty, get password options, randomize it and expose to the user"""
    global password
    
    if check_op_let.get() == 0 and check_op_num.get() == 0 and check_op_sym.get() == 0: 
        messagebox.showwarning(title="Warnning", message="You must to select you at least one password content (letter, symbol or numbers)")
    else:
        pass_options()
        random.shuffle(password)
        password = ''.join(map(str,password))
        pass_input.delete(0,END)
        pass_input.insert(0, password)
        pyperclip.copy(password)

def clear():
    """Clear all the entries and options"""
    web_input.delete(0,END)
    pass_input.delete(0,END)
    mail_input.delete(0,END)
    check_op_sym.set(1)
    check_op_num.set(1)
    check_op_let.set(1)
    insert_email()

def insert_email():
    """ Setup predefined email"""
    mail_input.insert(0, "contact@email.com")

def warn_message(msg):
    messagebox.showwarning(title="Warnning", message=msg)

def info_message(msg):
    messagebox.showwarning(title="Info", message=msg)

def save_in_file():
    """ Save the details (Website, email and password) in a local file"""
    if not web_input.get() or not mail_input.get() or not pass_input.get():
        warn_message("Some of the entries are empty")
    else:
        w = web_input.get().lower()
        m = mail_input.get().lower()
        p = pass_input.get()
        is_ok = messagebox.askyesno(title=w, message=f"These are the details entered: \n Email: {m}"
                                                f"\n Password: {p} \n Is it ok to save?")
        msg = {
            w: {
                "email": m,
                "password": p
            }
        }
        if is_ok:
            try:
                with open(FILENAME, "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(FILENAME, "w") as data_file:
                    json.dump(msg, data_file, indent=4)
            except json.decoder.JSONDecodeError:
                with open(FILENAME, "w") as data_file:
                    json.dump(msg, data_file, indent=4)
            else:
                data.update(msg)
                with open(FILENAME, "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                clear()

def find_password():
    """Search for an website entry in file database"""
    if not web_input.get():
        warn_message("The Website entry is empty")
    else:
        w = web_input.get().lower()
        try:
            with open(FILENAME, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            info_message("Database created, please try again")
            with open(FILENAME, "w") as data_file:
                pass
        except json.decoder.JSONDecodeError:
            info_message("No details for the website exists")
        else:
            if w in data:
                info_message(f"Website: {w}\n Email: {data[w]['email']}\n Password: {data[w]['password']}")
            else:
                warn_message(f"No website {w} found into database")
                
                
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=5)

label0 = Label(text="Website: ")
label0.grid(column=0, row=1)

label1 = Label(text="Email/Username: ")
label1.grid(column=0, row=2)

label2 = Label(text="Password: ")
label2.grid(column=0, row=3)

#Entry
web_input = Entry(width=30)
web_input.grid(column=1, row=1, columnspan=3)
web_input.focus()

mail_input = Entry(width=38)
mail_input.grid(column=1, row=2, columnspan=4)
insert_email()

pass_input = Entry(width=38)
pass_input.grid(column=1, row=3, columnspan=4)

# SpinBox
spinbox = Spinbox(from_=6, to=20, width=5)
spinbox.grid(column=1, row=4)

# RadioButton
check_op_let = IntVar(value=1)
check_op_sym = IntVar(value=1)
check_op_num = IntVar(value=1)

checkbutton_let = Checkbutton(text="Letter", variable=check_op_let)
checkbutton_sym = Checkbutton(text="Symbol", variable=check_op_sym)
checkbutton_num = Checkbutton(text="Number", variable=check_op_num)

checkbutton_let.grid(column=2, row=4)
checkbutton_sym.grid(column=3, row=4)
checkbutton_num.grid(column=4, row=4)

#Button
search_button = Button(text="Search", command=find_password)
search_button.grid(column=4, row=1)

gen_pass_button = Button(text="Generate Password", width=13, command=pass_generator)
gen_pass_button.grid(column=0, row=4)

add_button = Button(text="Add", width=25, command=save_in_file)
add_button.grid(column=0, row=5, columnspan=2)

clear_button = Button(text="Clear", width=25, command=clear)
clear_button.grid(column=2, row=5, columnspan=3)

window.mainloop()