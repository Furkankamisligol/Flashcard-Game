
from tkinter import *
import pandas
from random import choice
timer = ""
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
new_word = ""
words_data = pandas.read_csv("data/words.csv")
words = words_data.to_dict(orient="records")
number_of_words = len(words)


def random_new_word():
    global new_word
    new_word = choice(words)
    new_f_word = new_word["French"]
    new_t_word = new_word["Türkçe"]
    french_card.itemconfig(French_word, text=f"{new_f_word}")
    turkish_card.itemconfig(Turkish_word, text=f"{new_t_word}")
    new_french_card()


def new_french_card():
    global timer
    turkish_card.grid_remove()
    french_card.grid(row=1, column=0, columnspan=2)
    timer = window.after(3000, new_turkish_card)


def new_turkish_card():
    french_card.grid_remove()
    turkish_card.grid(row=1, column=0, columnspan=2)


def delete_word_and_next_card():
    global timer, new_word
    words.pop(words.index(new_word))
    window.after_cancel(timer)
    random_new_word()
    score()


def next_card():
    global timer
    window.after_cancel(timer)
    random_new_word()
    score()


def score():
    score1 = number_of_words - len(words)
    score_label.config(text=f"{score1}/{number_of_words}")


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg="#B1DDC6")
french_side = PhotoImage(file="images/card_front.png")
turkish_side = PhotoImage(file="images/card_back.png")
image_right = PhotoImage(file="images/right.png")
image_wrong = PhotoImage(file="images/wrong.png")

french_card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
french_card.create_image(400, 263, image=french_side)
french_card.create_text(400, 150, text="Français", fill="black", font=(FONT_NAME, 40, "italic"))
French_word = french_card.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
french_card.grid(row=1, column=0, columnspan=2)


turkish_card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
turkish_card.create_image(400, 263, image=turkish_side)
turkish_card.create_text(400, 150, text="Türkçe", fill="white", font=(FONT_NAME, 40, "italic"))
Turkish_word = turkish_card.create_text(400, 263, text="", fill="white", font=(FONT_NAME, 60, "bold"))


right_button = Button(image=image_right, highlightthickness=0, command=delete_word_and_next_card)
right_button.grid(row=2, column=1)
wrong_button = Button(image=image_wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=2, column=0)

score_label = Label(text=f"0/{number_of_words}", font=(FONT_NAME, 20, "bold"), bg="#B1DDC6", highlightthickness=0)
score_label.grid(row=0, column=0)


random_new_word()


window.mainloop()
