import tkinter as tk
import random




# def guess(event):
#     global attempts
#     print("Работает")
#     number = entry.get()
#     if number == "":
#         label["text"] = "Введи число от 1 до 100"
#     else:
#         if attempts > 0:
#             attempts -= 1
#             attempts_label["text"] = f"Количество попыток: {attempts}"
#             number = int(number)
#             if number == secret_number:
#                 label["text"] = "Поздравляю, ты угадал!"
#                 attempts = 0
#                 guess_button.configure(state=tk.DISABLED)
#                 reset_button.configure(state=tk.NORMAL)
#             if number < secret_number:
#                 label["text"] = "Загаданное число больше!"
#             if number > secret_number:
#                 label["text"] = "Загаданное число меньше!"
#         entry.delete(0, "end")
#         if attempts == 0:
#             guess_button.configure(state=tk.DISABLED)
#             reset_button.configure(state=tk.NORMAL)

def guess(event):
    global attempts
    print("Работает")
    number = entry.get()
    if number == "":
        label["text"] = "Введи число от 1 до 100"
    else:
        if attempts > 0:
            attempts -= 1
            attempts_label["text"] = f"Количество попыток: {attempts}"
            number = int(number)
            if number == secret_number:
                label["text"] = "Поздравляю, ты угадал!"
                attempts = 0
                guess_button.configure(state=tk.DISABLED)
                reset_button.configure(state=tk.NORMAL)
            if number < secret_number:
                label["text"] = "Загаданное число больше!"
            if number > secret_number:
                label["text"] = "Загаданное число меньше!"
        entry.delete(0, "end")
        if attempts == 0:
            guess_button.configure(state=tk.DISABLED)
            reset_button.configure(state=tk.NORMAL)

def reset():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 10
    attempts_label["text"] = f"Количество попыток: {attempts}"
    label["text"] = "Введи число от 1 до 100"
    entry.delete(0, "end")
    guess_button.configure(state=tk.NORMAL)
    reset_button.configure(state=tk.DISABLED)

window = tk.Tk()
window.geometry("300x300")
window.title("Угадай число")

label = tk.Label(window, text="Угадай число от 1 до 100",)
label.place(x=30, y=0)



entry = tk.Entry(window)
entry.place(x=40,y=50)
entry.focus_set()

guess_button = tk.Button(window, text="Проверить", width=17, command=lambda e="<Return>": guess(e))
# guess_button = tk.Button(window, text="Проверить", width=17, command= guess)
guess_button.place(x=35, y=80)

reset_button = tk.Button(window, text="Играть снова",width=17, command=reset, state=tk.DISABLED)
reset_button.place(x=35,y=110)

window.bind("<Return>", guess)
# secret_number = random.randint(1,100)
secret_number = 5
attempts = 10
attempts_label = tk.Label(window, text=f"Количество попыток: {attempts}")
attempts_label.place(x=30, y=30)


window.mainloop()