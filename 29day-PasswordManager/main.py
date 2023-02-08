from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

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
    check_op_sym.set(0)
    check_op_num.set(0)
    check_op_let.set(0)
    insert_email()

def insert_email():
    """ Setup predefined email"""
    mail_input.insert(0, "contact@email.com")

def save_in_file():
    """ Save the details (Website, email and password) in a local file"""
    FILENAME = "password_database.txt"
    if not web_input.get() or not mail_input.get() or not pass_input.get():
        messagebox.showwarning(title="Warnning", message="Some of the entries are empty")
    else:
        w = web_input.get()
        m = mail_input.get()
        p = pass_input.get()
        is_ok = messagebox.askyesno(title=w, message=f"These are the details entered: \n Email: {m}"
                                                f"\n Password: {p} \n Is it ok to save?")
        if is_ok:
            msg = f"{w} | {m} | {p}"
            with open(f"{FILENAME}", mode='a') as password_file:
                password_file.write(msg + "\n")
            clear()
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

label0 = Label(text="Website: ")
label0.grid(column=0, row=1)

label1 = Label(text="Email/Username: ")
label1.grid(column=0, row=2)

label2 = Label(text="Password: ")
label2.grid(column=0, row=3)

#Entry
web_input = Entry(width=38)
web_input.grid(column=1, row=1, columnspan=4)
web_input.focus()

mail_input = Entry(width=38)
mail_input.grid(column=1, row=2, columnspan=4)
insert_email()

pass_input = Entry(width=38)
pass_input.grid(column=1, row=3, columnspan=4)

# SpinBox
spinbox = Spinbox(from_=4, to=20, width=5)
spinbox.grid(column=1, row=4)

# RadioButton
check_op_let = IntVar()
check_op_sym = IntVar()
check_op_num = IntVar()

checkbutton_let = Checkbutton(text="Letter", variable=check_op_let)
checkbutton_sym = Checkbutton(text="Symbol", variable=check_op_sym)
checkbutton_num = Checkbutton(text="Number", variable=check_op_num)

checkbutton_let.grid(column=2, row=4)
checkbutton_sym.grid(column=3, row=4)
checkbutton_num.grid(column=4, row=4)

#Button
gen_pass_button = Button(text="Generate Password", width=13, command=pass_generator)
gen_pass_button.grid(column=0, row=4)

add_button = Button(text="Add", width=25, command=save_in_file)
add_button.grid(column=0, row=5, columnspan=2)

clear_button = Button(text="Clear", width=25, command=clear)
clear_button.grid(column=2, row=5, columnspan=3)

window.mainloop()