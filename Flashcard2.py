from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data = {}

# ---------------------------- PANDAS ------------------------------- #

try:
    data = pandas.read_csv("./data/chem.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/chem1.csv")
finally:
    flash_cards_to_learn = data.to_dict(orient="records")
# ---------------------------- NEXT CARD ------------------------------- #


def next_card():
   global waiting_to_flip, current_card
   window.after_cancel(waiting_to_flip)

   current_card = random.choice(flash_cards_to_learn)
   flip_card(card_front_img, 'front', 'black')
   waiting_to_flip = window.after(3000, flip_card, card_back_img, 'back', 'white')

# ---------------------------- FLIP CARD ------------------------------- #


def flip_card(img, front, fill):
    flashcard.itemconfig(image, image=img)
    flashcard.itemconfig(title, text=front, fill=fill)
    flashcard.itemconfig(word, text=current_card[front], fill=fill)


def update_flash_cards_to_learn():
    flash_cards_to_learn.remove(current_card)
    cards_to_learn = pandas.DataFrame(flash_cards_to_learn)
    cards_to_learn.to_csv("./data/chem.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Learn Chemistry with Flashcards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front_img = PhotoImage(file="./pictures/card_front.png")
card_back_img = PhotoImage(file="./pictures/card_back.png")

waiting_to_flip = window.after(3000, flip_card, card_back_img, 'back', 'white')

# GRID
# row 1
flashcard = Canvas(width=830, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
image = flashcard.create_image(415, 265)

title = flashcard.create_text(400, 150, text="", font=("Helvetic", 35, "italic"))
word = flashcard.create_text(400, 265, text="", font=("Helvetica", 55, "bold"))

flashcard.grid(row=0, column=0, columnspan=2)

# row 2 add difficulty function for how many times counted
wrong_btn_img = PhotoImage(file="./pictures/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_btn_img = PhotoImage(file="./pictures/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, command=update_flash_cards_to_learn)
right_btn.grid(row=1, column=1)

next_card()
window.mainloop()
