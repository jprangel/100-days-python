from tkinter import *
from tkinter import messagebox
import pandas
import random

CARD_X = 400
CARD_Y = 263

BACKGROUND_COLOR = "#B1DDC6"
FLIP_BG_COLOR = "#91c2af"
unknow_word_deck_dict = {}
know_word_deck_dict = {}

def unknow_word_deck():
    """ Append in a dict the words that are unknown by the user"""
    window.after_cancel(flip_time)
    unknow_word_deck_dict[word] = translation
    check_remaning_words()
    
def know_word_deck():
    """ Append in a dict the words that are known by the user"""
    know_word_deck_dict[word] = translation
    window.after_cancel(flip_time)
    check_remaning_words()
    
def check_remaning_words():
    """ Check if the user saw all the words in the words database (dict)"""
    sum = int(len(unknow_word_deck_dict)) + int(len(know_word_deck_dict))
    if sum < int(len(words_dict)):
        create_new_flash_card(language)
    else:
        is_ok = messagebox.askyesno(title="Congrats", message="Congrats !! you finished our words database,\n do you wanna restart?")
        if is_ok:
            clear()
            create_new_flash_card(language)
        else:
            window.destroy()

def clear():
    """ Clear the dicts to restart the app"""
    unknow_word_deck_dict.clear()
    know_word_deck_dict.clear()
        
def set_language(lang):
    """ Set the language and load the word database (dict) for the languages choosed"""
    global language, data_csv
    language = lang
    if lang == "Romanian":
        set_ro_label()
        click_start_msg()
        data_csv = pandas.read_csv("data/ro_en_data.csv")
    else:
        set_pt_label()
        click_start_msg()
        data_csv = pandas.read_csv("data/pt_en_data.csv")
    
def set_ro_label():
   """" Update the label to show the language choosed by the user"""
   title.config(text="Romanian", bg="white", fg="black")

def set_pt_label():
    """" Update the label to show the language choosed by the user"""
    title.config(text=f"Brazilian Portuguese", bg="white", fg="black")
    
def click_start_msg():
    """ Show a label for the user click in the start button"""
    word_label.config(text="Click START button to proceed", bg="white", font=("Arial", 30, "bold"))
    
def start(language):
    """ Start to flip the card for the user"""
    if not language:
        messagebox.showwarning(title="Warn", message="Opss... Please choose one language before click START")
    else:
        create_new_flash_card(language)
        
def create_new_flash_card(language):
    """ Choose a new word and show in flip card"""
    score.config(text=f"Score: Know words: {len(know_word_deck_dict)} | Unknow words: {len(unknow_word_deck_dict)} | Word database: 200")
    if language == "Romanian":
        set_ro_label()
    elif language == "Portuguese":
        set_pt_label()
    canvas.create_image(CARD_X, CARD_Y, image=card_front)
    canvas.grid(column=0, row=1, columnspan=3, rowspan=2)
    global flip_time
    try:
        word = get_random_word()
    except:
        print("No dict")
    else:
        global translation
        translation = words_dict[word]
        word_label.config(text=word, bg="white", fg="black", font=("Arial", 60, "bold"))
        flip_time = window.after(5000, word_translation)

def get_random_word():
    """ Get a random word from the word database (dict)"""
    global words_dict, word
    words_dict = {row.original_word:row.translated_word for index,row in data_csv.iterrows()}
    word = (random.choice(list(words_dict.keys())))
    while word in know_word_deck_dict:
        word = (random.choice(list(words_dict.keys())))
    return word
        
def word_translation():
    """ Flip the card and show the word in English for the user"""
    canvas.create_image(CARD_X, CARD_Y, image=card_back)
    canvas.grid(column=0, row=1, columnspan=3, rowspan=2)
    title.config(text="English", bg=FLIP_BG_COLOR, fg="white")
    word_label.config(text=translation, bg=FLIP_BG_COLOR, fg="white")
   
# UI
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=30, bg=BACKGROUND_COLOR)

score = Label(text=f"Score: Know words: {len(know_word_deck_dict)} | Unknow words: {len(unknow_word_deck_dict)} | Word database: 200", bg=BACKGROUND_COLOR, font=("Arial", 20, "normal"))
score.grid(column=0, row=0, columnspan=3, padx=0, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas.create_image(CARD_X, CARD_Y, image=card_front)
canvas.grid(column=0, row=1, columnspan=3, rowspan=2)

b_right_img = PhotoImage(file="images/right.png")
b_right = Button(image=b_right_img, borderwidth=0, highlightthickness=0 , bg=BACKGROUND_COLOR, command=know_word_deck)
b_right.grid(column=0, row=3)

language = ""
start_button = Button(text="START", width="20", height="4", font=("Arial", 20, "bold"), borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR, command= lambda: start(language))
start_button.grid(column=1, row=3)

b_wrong_img = PhotoImage(file="images/wrong.png")
b_wrong = Button(image=b_wrong_img, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR, command=unknow_word_deck)
b_wrong.grid(column=2, row=3)

title = Label(text="Welcome", bg="white", font=("Arial", 40, "italic"))
title.place(relx=0.45, rely=0.3, anchor = 'center')

word_label = Label(text="Choose the language", bg="white", font=("Arial", 60, "bold"))
word_label.place(relx=0.45, rely=0.5, anchor = 'center')

flag_br_img = PhotoImage(file="images/br_flag.png")
flab_br = Button(image=flag_br_img, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR, command= lambda: set_language("Portuguese"))
flab_br.grid(column=4, row=1)

flag_ro_img = PhotoImage(file="images/ro_flag.png")
flab_ro = Button(image=flag_ro_img, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR, command= lambda: set_language("Romanian"))
flab_ro.grid(column=4, row=2)

window.mainloop()