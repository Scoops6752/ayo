from tkinter import *

# This opening code is to create a window and menu options. I'm going for a
# basic framework here in which everything else will fall under.


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


def finished():
    root.destroy()


# Variables used throughout the code
top_color = 'white'
bottom_color = 'grey'
background_color = 'black'
button_color = 'white'

card_num = 0
# Just add any question you want,
questions = [
    'What is 1+1',
]
answers = [
    '2',
]
fanswers1 = [
    '5',
]
fanswers2 = [
    '7',
]
fanswers3 = [
    '9',
]


root = Tk()
root.title('Flashcard Application')
root.resizable(width=0, height=0)
center_window(600, 350)
root.configure(bg=background_color)
# Makes sure the items in the root grid are stretched to capacity
root.grid_rowconfigure(0, weight=3)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)


def clicked_correct():
    try:
        global card_num
        card_num += 1
        question_label.configure(text=questions[card_num])
        btn1.configure(text=answers[card_num])
        btn2.configure(text=fanswers1[card_num])
        btn3.configure(text=fanswers2[card_num])
        btn4.configure(text=fanswers3[card_num])
    except IndexError:
        finished()


def clicked_incorrect():
    question_label.configure(text='Incorrect. Try Again.')


# Menu functions
def res():
    global card_num
    card_num = 0
    question_label.configure(text=questions[0])
    btn1.configure(text=answers[0])
    btn2.configure(text=fanswers1[0])
    btn3.configure(text=fanswers2[0])
    btn4.configure(text=fanswers3[0])


# Menu bar options
menu = Menu(root)
reset = Menu(menu, tearoff=0)
reset.add_command(label='Reset', command=res)
menu.add_cascade(label='File', menu=reset)

menu.add_command(label='Edit')
root.config(menu=menu)


# Creates root frame containers
top_frame = Frame(root, bg=top_color, width=600, height=225)
bottom_frame = Frame(root, bg=bottom_color, width=600, height=125)
# Places root frame containers
top_frame.grid(row=0, sticky='wens', padx=5, pady=(5, 0))
bottom_frame.grid(row=1, sticky='wens', padx=5, pady=5)

# Makes sure items in the top frame grid are stretched to capacity
top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_columnconfigure(0, weight=1)
# Creates top frame widgets
question_label = Label(top_frame, bg=top_color, text=questions[card_num], font=('Arial Bold', 30))

# Place top frame widgets
question_label.grid(row=0, column=0)

# Makes sure items in bottom frame grid are stretched to capacity
bottom_frame.grid_rowconfigure(0, weight=1)
bottom_frame.grid_rowconfigure(1, weight=1)
bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=1)


# Creates bottom widgets
btn1 = Button(bottom_frame, text=answers[card_num], bg=button_color, command=clicked_correct)
btn2 = Button(bottom_frame, text=fanswers1[card_num], bg=button_color, command=clicked_incorrect)
btn3 = Button(bottom_frame, text=fanswers2[card_num], bg=button_color, command=clicked_incorrect)
btn4 = Button(bottom_frame, text=fanswers3[card_num], bg=button_color, command=clicked_incorrect)

# Place top frame widgets
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)

root.mainloop()
