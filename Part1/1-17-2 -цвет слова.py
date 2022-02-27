# импорт tkinter
# создаем окно, название, размеры
# создаем надписи и окно:
# 1 - Введи цвет слова, а не слово! Жми Enter, чтобы играть.
# 2 - colorsys
# 3 - поле для ввода цвета
# задаем фокус на поле с вводом при помощи .focus_set()
# список с цветами
# создаем функцию new_word которая генерирует цвет текста и текст
# Создаем функцию по проверке check
# создаем window.bind("<Return>", check) чтобы вместо кнопки нажимать на клавишу ENTER

# создаем счет
# добавляем переменные колличество успешных и неуспешных ответов
# создаем поля для вывода колличества правильных и неправильных ответов
#
# функция проверки:
#     берем слово из поля и цвет текста из поля color
#     сравниваем, если равны увеличиваем score на 1
#     если не равны увеличиваем fails на 1


# создаем время
# переменная с временем
# создаем поле с текстом оставшегося времени
# сделаем функцию таймера - используем глобальную переменную и проверяем, если она больше 0 - уменьшаем, и обновляем текст на надписи таймера
# Вызываем новую функцию в конце программы:
# команда after,
# Обновим функцию check, теперь мы будем выполнять проверку только если оставшееся время больше 0
# Первый вызов функции таймера тоже можно прописать с задержкой:

import tkinter as tk
import tkinter.messagebox as tmb
import random

def timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label["text"] = f"Осталось секунд: {time_left}"
        time_label.after(1000, timer)
        tmb.askokcancel()
    ''' ДЗ
    else:
        tmb.showinfo("Конец игры", "Время вышло")
    '''


def new_word():
    color_label["fg"] = random.choice(colors)
    color_label["text"] = random.choice(colors)


def check(event):
    # print("Проверка")
    global score
    global fails
    if time_left > 0:
        user_color = entry.get()
        word_color = color_label["fg"]
        if user_color == word_color:
            print("да")
            score += 1
            score_label["text"] = f"Правильно: {score}"
        else:
            print("нет")
            fails += 1
            fails_label["text"] = f"Неправильно: {fails}"
        new_word()
        entry.delete(0, "end")
    ''' ДЗ
    else:
        if score>fails:
            tmb.showinfo("Хороший результат", "Ты молодец!")
        else:
            tmb.showinfo("Неважный результат", "В следующий раз получится лучше.")
     '''


window = tk.Tk()
window.title("Назови цвет")
window.geometry("350x250")

colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "white", "purple", "brown"]
score = 0
fails = 0
time_left = 5





instructions = tk.Label(window, text="Введи цвет слова, а не слово! Жми Enter, чтобы играть.", font=("Helvetica", 10))
instructions.place(x=10, y=10)

color_label = tk.Label(window, text="color", font=("Helvetica", 60))
color_label.place(x=10, y=80)

entry = tk.Entry(window, font=("Helvetica", 10))
entry.place(x=10, y=180)
entry.focus_set()

score_label = tk.Label(window, text=f"Правильно: {score}", font=("Helvetica", 10))
score_label.place(x=10, y=40)

fails_label = tk.Label(window, text=f"Неправильно: {fails} ", font=("Helvetica", 10))
fails_label.place(x=10, y=60)

time_label = tk.Label(window, text=f"Осталось секунд: {time_left}")
time_label.place(x=10, y=210)

new_word()
window.bind("<Return>", check)
time_label.after(1000, timer)
window.mainloop()




