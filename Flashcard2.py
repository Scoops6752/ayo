from tkinter import *
import sqlite3
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data = {}

# ---------------------------- DATABASE ------------------------------- #
#creation of database
db_1 = sqlite3.connect('Chem_tutor.db')

#Create cursor i.e. Cursor is what interacts with the database
c1 = db_1.cursor()




#create table

#c1.execute("""CREATE TABLE questions (
#        Question text,
#        Answer text
#        )""")

#c1.execute("INSERT INTO questions VALUES ('NaOH', 'Sodium hydroxide')")

c1.execute("SELECT * FROM questions WHERE Question='NaOH'")
print(c1.fetchone())
#commit changes
db_1.commit()

#close connection
db_1.close()
# ---------------------------- NEXT CARD ------------------------------- #


#def next_card():
#    global waiting_to_flip, current_card
#    window.after_cancel(waiting_to_flip)

#    current_card = random.choice(vocabulary_to_learn)
#    flip_card(card_front_img, 'French', 'black')
#    waiting_to_flip = window.after(3000, flip_card, card_back_img, 'English', 'white')

# ---------------------------- FLIP CARD ------------------------------- #


#def flip_card(img, lang, fill):
#    flashcard.itemconfig(image, image=img)
#    flashcard.itemconfig(title, text=lang, fill=fill)
#    flashcard.itemconfig(word, text=current_card[lang], fill=fill)


#def update_vocabulary_to_learn():
#    vocabulary_to_learn.remove(current_card)
#    to_learn_data = pandas.DataFrame(vocabulary_to_learn)
#    to_learn_data.to_csv("./data/words_to_learn.csv", index=False)
#    next_card()


# ---------------------------- UI SETUP ------------------------------- #


#window = Tk()
#window.title("Learn French with Flashcards")
#window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

#card_front_img = PhotoImage(file="./images/card_front.png")
#card_back_img = PhotoImage(file="./images/card_back.png")

#waiting_to_flip = window.after(3000, flip_card, card_back_img, 'English', 'white')

# GRID
# row 1
#flashcard = Canvas(width=830, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
#image = flashcard.create_image(415, 265)

#title = flashcard.create_text(400, 150, text="", font=("Helvetic", 35, "italic"))
#word = flashcard.create_text(400, 265, text="", font=("Helvetica", 55, "bold"))

#flashcard.grid(row=0, column=0, columnspan=2)

# row 2
#wrong_btn_img = PhotoImage(file="./images/wrong.png")
#wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=next_card)
#wrong_btn.grid(row=1, column=0)

#right_btn_img = PhotoImage(file="./images/right.png")
#right_btn = Button(image=right_btn_img, highlightthickness=0, command=update_vocabulary_to_learn)
#right_btn.grid(row=1, column=1)

#  next_card()
#window.mainloop()
