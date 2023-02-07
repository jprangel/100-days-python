from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
timer = "00:00:00"
reps = 0
reset_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(reset_timer)
    canvas.itemconfig(timer_text, text=timer)
    check_mark = ""
    label_timer.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        label_timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label_timer.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        label_timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"00:{count_min}:{count_sec}")
    if count > 0:
        global reset_timer
        reset_timer = window.after(1000, countdown, count - 1)
    else:
        start()
        global check_mark
        check_mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_mark += "✓"
        label_check = Label(text=check_mark, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
        label_check.grid(column=1, row=4)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label0 = Label(text="", bg=YELLOW)
label0.grid(column=0, row=0)

label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "normal"))
label_timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 125, text=timer, fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

button_start = Button(text="Start", highlightthickness=0, bg=YELLOW, command=start)
button_start.grid(column=0, row=3)

button_reset = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset)
button_reset.grid(column=3, row=3)

window.mainloop()