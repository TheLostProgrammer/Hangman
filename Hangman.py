from tkinter import *
from PIL import ImageTk, Image
from random import *
from words import words

window = Tk()

title = Label(window, text="Enter one word for your opponent to guess:", font=("Helvetica", 14, "bold", "italic"))
title.grid(row=0, column=1)
wordInput = Entry(window, width=50)
wordInput.grid(row=1, column=1, ipady=3)

letters_title = Label(window, text="Used Letters", font=("Helvetica", 20, "bold", "underline"), foreground="grey")
letters_title.grid(row=3, column=1)

start_image = Image.open("images/stage0.png")
start_image = start_image.resize((250, 250), Image.ANTIALIAS)
start_image = ImageTk.PhotoImage(start_image)
start_panel = Label(window, image=start_image)
start_panel.image = start_image
start_panel.grid(row=5, column=1)

word_display = Label(window, text="Word will show up here...", foreground="#5E5E5E")
word_display.grid(row=6, column=1)

letters = Label(window, text="", foreground="grey")
letters.grid(row=4, column=1)

playerText = Label(window, text="Enter a letter:", font=("Helvetica", 14, "bold", "italic")).grid(row=7, column=1)
player = Entry(window, width=50)
player.grid(row=8, column=1, ipady=3)


def scaffold_interface(total):
    if int(total) == 0:
        img = Image.open("images/stage1.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 1:
        img = Image.open("images/stage2.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 2:
        img = Image.open("images/stage3.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 3:
        img = Image.open("images/stage4.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 4:
        img = Image.open("images/stage5.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 5:
        img = Image.open("images/stage6.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 6:
        img = Image.open("images/stage7.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 7:
        img = Image.open("images/stage8.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 8:
        img = Image.open("images/stage9.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 9:
        img = Image.open("images/stage10.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 10:
        img = Image.open("images/stage11.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 11:
        img = Image.open("images/stage12.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 12:
        img = Image.open("images/stage13.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)
    elif total == 13:
        img = Image.open("images/stage14.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=5, column=1)


buttonWidth = 10
used_letters = []
count = -1


def get_word():
    global word
    global reveal
    if button_state:
        word = choice(words)
    else:
        word = wordInput.get().lower()
        if len(word) > 14:
            title.config(text="The word was longer than 14 characters. Enter a new word:")
        title.config(text="Enter a word for your opponent to guess:")
    reveal = list(len(word) * "_")
    wordInput.delete(0, END)
    letters.config(text="")
    used_letters.clear()
    print(word)
    word_display.config(text=reveal, font=("Helvetica", 100))
    window.update()


button_state = False


def switch():
    global button_state
    if button_state:
        button_state = False

        print(button_state)
    else:
        button_state = True
        wordInput.config(state='disabled')

        print(button_state)


def appearance():
    global count
    global button_state
    print(word)
    letter = player.get().lower()
    for i in range(len(word)):
        if letter == word[i]:
            reveal[i] = letter
    word_display.config(text=reveal, font=("Helvetica", 100))

    if len(letter) == 1:
        if str(letter) in str(word):
            print("Correct")

        elif str(letter) not in str(word):
            print("\nWrong")
            count += 1
            print(count)
            if letter not in used_letters:
                scaffold_interface(count)
        if letter not in used_letters:
            used_letters.append(letter)

        result = "".join(letter for letter in used_letters)
        letters.config(text="\n".join([result[i:i + 26].upper() for i in range(0, len(result), 26)]),
                       font=("Helvetica", 20))
        letters_title.config(text=f"Used Letters ({len(result)})", foreground="grey")
        print("The length is: " + str(len(result)))
        if "".join(reveal) == word:
            button_state = False
            wordInput.config(state='normal')
            letters_title.config(text="")
            used_letters.clear()
            letters.config(text="")
            img = Image.open("images/stage0.png")
            img = img.resize((250, 250), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = Label(window, image=img)
            panel.image = img
            panel.grid(row=5, column=1)
            word_display.config(text="You guessed the correct word. "
                                     "Game Over!\nPress \"New Game\" to play again.", font=("Helvetica", 20))
        if count > 13:
            button_state = False
            wordInput.config(state='normal')
            count = -1
            letters_title.config(text="")
            used_letters.clear()
            letters.config(text="")
            img = Image.open("images/stage0.png")
            img = img.resize((250, 250), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = Label(window, image=img)
            panel.image = img
            panel.grid(row=5, column=1)
            word_display.config(text=f"You ran out of guesses. The word was "
                                     f"\"{word}\"\nPress \"New Game\" to play again.", font=("Helvetica", 20))
    player.delete(0, END)


def close():
    window.quit()


def newgame():
    global count
    global button_state
    count = -1
    wordInput.config(state='normal')
    letters_title.config(text="")
    used_letters.clear()
    wordInput.delete(0, END)
    letters.config(text="")
    used_letters.clear()
    word_display.config(text="Word will show up here...", font=("Helvetica", 14))
    img = Image.open("images/stage0.png")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.image = img
    panel.grid(row=5, column=1)
    window.update()
    button_state = False


getwordButton = Button(window, text="Enter", command=get_word, width=10).grid(row=2, column=1, ipady=3)
single_player_button = Button(window, text="Single Player", command=switch, width=10).grid(row=2, column=2, ipady=3)
quitButton = Button(window, text="Quit", width=buttonWidth, command=close).grid(row=1, column=2, ipady=3)
newgameButton = Button(window, text="New Game", width=buttonWidth, command=newgame).grid(row=1, column=0, ipady=3)
appearanceButton = Button(window, text="Enter", command=appearance, width=10).grid(row=9, column=1, ipady=3)


window.mainloop()
