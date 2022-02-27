import tkinter as tk
import tkinter.messagebox as tmb
import random

def check_letter():
    global num
    global atteppts
    letter = entry_letter.get()
    letters.append(letter)
    print(word)
    show_word = ""
    for char in word:
        if char in letters:
            show_word += char
        else:
            show_word += "*"

    label_word["text"] = show_word
    entry_letter.delete(0, "end")
    if show_word == word:
        print("Победа!!!")
        tmb.showinfo("Победа", "Ты угадал слово!")
        new_game()
    print(num)
    num += 1
    if letter  not in word:
        atteppts -= 1
        label_attempts["text"] = f"У тебя осталось {atteppts} попыток"

    if atteppts == 0:
        tmb.showinfo("Проигрышь", f"Ты проиграл! \n{word}")
        new_game()



def new_game():
    global word
    global letters
    global  atteppts
    atteppts = 3
    letters = []
    word = random.choice(words)
    label_word["text"] = "Здесь будет слово"
    label_attempts["text"] = f"У тебя осталось {atteppts} попыток"


tmb.askokcancel()
window = tk.Tk()
window.title("Угадай cлово")
window.geometry("300x200")

with open("text/words.txt", 'r', encoding='utf8') as file:
    data = file.read()
words = data.split()
word = random.choice(words)
letters = []
num = 1
atteppts = 3


label_word = tk.Label(window, text="Здесь будет слово", font=("Arial", 15))
label_word.place(x=70, y=20)

entry_letter = tk.Entry(window, width=5, font=("Arial", 10))
entry_letter.place(x=130, y=80)

check_button = tk.Button(window, text="Проверить букву", font=("Arial", 10), command = check_letter)
check_button.place(x=100, y=120)

label_attempts = tk.Label(window, text=f"У тебя осталось {atteppts} попыток", font=("Arial", 10))
label_attempts.place(x=50, y=170)




window.mainloop()
