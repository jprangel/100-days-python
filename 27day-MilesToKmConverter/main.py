from tkinter import *

window = Tk()
window.title("KM to Miles converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

def calculate():
    miles = input.get()
    km = float(miles) * 1.609
    label3.config(text=int(km))

label = Label(text="")
label.grid(column=0, row=0)

input = Entry(width=10)
input.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal")
label2.grid(column=0, row=1)

label3 = Label(text="")
label3.grid(column=1, row=1)

label4 = Label(text="KM")
label4.grid(column=2, row=1)

button = Button(text="calculate", command=calculate)
button.grid(column=1, row=2)












window.mainloop()