from tkinter import*

main = Tk()
main.title("Flash Card Maniak")
main.geometry("520x600")

#create menu

def create_card():
    hide_all_frame()
    create_button()
    frontside_input()
    card_frame.pack(fill="both", expand=1)


def quiz_card():
    hide_all_frame()
    quiz_answer()
    card_frame.pack(fill="both", expand=1)


def create_button():
    button = Button(card_frame, text="Create", command=create_button, padx=20, pady=10). grid(row=3, column=2)
    button = Button(card_frame, text="Next", command=next_button, padx=20, pady=10). grid(row=3, column=3)
    button = Button(card_frame, text="Previous", command=prev_button, padx=20, pady=10). grid(row=3, column=1)


def frontside_input():
    frontside = Text(main, width= 200)
    frontside.pack()

def quiz_answer():
    label = Label(main, text="This is where the text should be").pack()
    button = Button(card_frame, text="Submit", padx=20, pady=10).grid(row=5, column=2)
    button = Button(card_frame, text="Previous", command=prev_button, padx=20, pady=10).grid(row=5, column=1)
    button = Button(card_frame, text="Next", command=next_button, padx=20, pady=10). grid(row=5, column=3)
    quizanswer = Entry(main, width = 100).pack()

def prev_button():
    pass

def next_button():
    pass

def filler_row():
    pass
    #filler_row = Label(card_frame, text="                                ").grid(row=2, column=1)
    #filler_row = Label(card_frame, text="                                ").grid(row=2, column=2)
    #filler_row = Label(card_fr\ame, text="                                ").grid(row=1, column=0)
    #filler_row = Label(card_frame, text="                                ").grid(row=1, column=3)


def hide_all_frame():
    for widget in card_frame.winfo_children():
        widget.destroy()


my_menu = Menu(main)
main.config(menu=my_menu)


card_menu = Menu(my_menu)
my_menu.add_cascade(label="Flashcard", menu=card_menu)
card_menu.add_command(label="Create Flashcard", command=create_card)
card_menu.add_command(label="Quiz Flashcard", command=quiz_card)
card_menu.add_separator()
card_menu.add_command(label="Exit", command=main.quit)

card_frame = Frame(main, width=200, height=400)

main.mainloop()
