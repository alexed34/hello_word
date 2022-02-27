import tkinter as tk
import tkinter as tk
import random

def new_word():
    color_label["fg"] = random.choice(colors) # задаем случайный цвет слова из списка и присваеваем обьекту color_label
    color_label["text"] = random.choice(colors) # задаем случайное слово из списка и присваеваем обьекту color_label


def check(event):
    print("Проверка")
    global score # правильные попытки
    global fails  # неправильные попытки

    if time_left > 0:
        user_color = entry.get() # вытаскиваем слово из поля
        word_color = color_label["fg"] #  вытаскиваем цвет слова
        if user_color == word_color:
            print("да")
            score += 1
            score_label["text"] = f"Правильно: {score}"
        else:
            print("нет")
            fails += 1
            fails_label["text"] = f"Неправильно: {fails}"
        new_word() # генерируем новое слово
        entry.delete(0, "end") # очищаем текст в поле ввода

def timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label["text"] = f"Осталось секунд: {time_left}"
        time_label.after(1000, timer)


window = tk.Tk()
window.title("Назови цвет")
window.geometry("350x250")
score = 0
fails = 0
time_left = 15
colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "purple", "brown", "white"]

instructions = tk.Label(window, text="Введи цвет слова, а не слово! Жми Enter, чтобы играть.", font=("Helvetica", 10))
instructions.place(x=10, y=10)

color_label = tk.Label(window,text="color", font=('Helvetica', 60))
color_label.place(x=10, y=80)

entry = tk.Entry(window, font=('Helvetica', 10))
entry.place(x=10, y=180)

score_label = tk.Label(window, text=f"Правильно: {score}", font=("Helvetica", 10))
score_label.place(x=10, y=40)

fails_label = tk.Label(window, text=f"Неправильно: {fails} ", font=("Helvetica", 10))
fails_label.place(x=10, y=60)

time_label = tk.Label(window, text=f"Осталось секунд: {time_left}" )
time_label.place(x=10, y=210)

entry.focus_set()
new_word()
window.bind("<Return>", check)
#timer()
time_label.after(1000,timer) #у элементов окна есть команда after, которая позволяет выполнять указанную функцию через заданный промежуток времени в миллисекундах
window.mainloop()