BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random


# --------------------------------------save progress--------------------------------------
#rather than using french_words.csv, we should create a copy and use it so we can delete words that we know
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:

    to_learn = data.to_dict(orient='records')
#if there are no words left, then we should just create a brand new copy.

#if the check button was clicked, there should be a function that removes the word from the csv file.


# --------------------------------------import csv file--------------------------------------


# data = pandas.read_csv('data/french_words.csv')
# to_learn = data.to_dict(orient='records')
print(to_learn)
current_card = {}



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
        #i dont really get how does this count stuff work.
        #now it just takes a while to load a new card, but it then automatically sRR hows the english side.
        #and the card isnt flipping sides at all.
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    #translate
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv',index=False)
    next_card()









# --------------------------------------UI--------------------------------------
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = image=PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic') )
card_word = canvas.create_text(400, 263, text='trouve', font=('Ariel', 60, 'bold') )

canvas.grid(column=0, row=1, columnspan=2)


#unknownButton
wrong_photo = PhotoImage(file='images/wrong.png')
unknownButton = Button(image=wrong_photo, command=next_card)
unknownButton.grid(column=0, row=2, columnspan=1)

#checkButton
right_photo = PhotoImage(file='images/right.png')
checkButton = Button(image=right_photo,command=is_known)
checkButton.grid(column=1, row=2, columnspan=1)


window.mainloop()