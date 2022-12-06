from tkinter import *
from tkinter import ttk
import random

FONT = ('Arial', 60, 'bold')

mult1 = 0
mult2 = 0
score_value = 0
result_value = 0


def create_first_question():
    global mult1, mult2
    mult1 = random.randint(1, 9)
    mult2 = random.randint(1, 9)
    question.config(text=f"{mult1} x {mult2}")


def create_new_question():
    global mult1, mult2
    mult1 = random.randint(1, 9)
    mult2 = random.randint(1, 9)
    question.config(text=f"{mult1} x {mult2}")
    result.config(text="")
    answer.delete(first=0, last=END)


def show_result():
    global mult1, mult2
    result.config(text=f"= {mult1 * mult2}")


def check_result():
    global mult2, mult1, score_value
    res = int(answer.get())
    if (mult1 * mult2) == res:
        score_value += 1
        score.config(text=f"Puntuacion: {score_value}")
        canvas.itemconfigure(result_image,image=thumb_up)
    else:
        canvas.itemconfigure(result_image,image=thumb_down)



def compose_function(event):
    show_result()
    check_result()
    window.after(2000, create_new_question)


# def update_score():
#     global score_value
#     if check_result():
#         score_value += 1
#         score.config(text=f"{score_value}")


# ---------------------------------- GUI -------------------------------- #

window = Tk()
window.title("Multiply")
window.config(padx=50, pady=50)

# labels

score = Label(window, text="Puntuacion: ", pady=50, font=FONT, )
score.grid(row=0, column=0)

question = Label(window, text="Question", pady=100, font=FONT)
question.grid(row=1, column=0)

result = Label(window, text="", font=FONT, pady=100)
result.grid(row=1, column=1)

# Entry

answer = Entry(window, width=30, font=FONT)
answer.grid(row=2, column=0)
answer.focus()
window.bind('<Return>', compose_function)

# Canvas

thumb_up = PhotoImage(file="thumb_up.png")
thumb_down = PhotoImage(file="thumb_down.png")
canvas = Canvas(window, width=512, height=512)
result_image = canvas.create_image(250, 250, image=thumb_up)
canvas.grid(row=2, column=1)

create_first_question()

window.mainloop()
