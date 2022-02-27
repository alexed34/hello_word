# создаем окно tkinter
# открываем файл с словами и выбераем случайно одно слово
# создаем поле с словом
# создаем поле куда будем вставлять букву
# создаем кнопку проверить слово
# создаем поле с колличеством попыток
# создаем функцию вывод слова в программу
# реализуем печать отгаданной буквы
# проверка победы, break создать нельзя поэтому запускаем новая игра
# создать функцию запуска новой игры
# уменьшать попытки
# реализовать проигрышь


import tkinter
import  random


def check():
    global  attempts
    print('работает')
    text = ''
    litter = liter_entry.get()
    litters.append(litter)
    print(attempts)
    for i in word:
        if i in litters:
            text += i
        else:
            text += '*'
    text_lebel['text'] = text
    liter_entry.delete(0, "end")
    if text == word:
        text_lebel['text'] = f'{text},\n Победа'
        new_game()
    if litter not in word:
        attempts -= 1
        text_attempts['text'] = f'У вас осталось {attempts} попыток'
    if attempts == 0:
        text_attempts['text'] = f'вы проиграли'
        new_game()




def new_game():
    global word
    global litters
    global attempts
    word = random.choice(words)
    litters = []
    text_lebel['text'] = 'Новая игра \n здесь будет слово'
    attempts = 5


window = tkinter.Tk()
window.title('угодай слово')
window.geometry('300x300')
window.resizable()

with open ('text/words.txt', 'r', encoding='utf8') as file:
    words = file.read().split()


word = random.choice(words)
word = 'привет'
litters = []

attempts = 2

text_lebel = tkinter.Label(window, text='здесь будет слово', font=('Arial', 15))
text_lebel.place(x=50, y=20)

liter_entry = tkinter.Entry(window, width=5, font=('Arial', 15))
liter_entry.place(x=80, y=100)

liter_button = tkinter.Button(window, text='проверить букву', font=('Arial', 10), command=check)
liter_button.place(x=80, y=150)

text_attempts = tkinter.Label(window, text=f'У вас осталось {attempts} попыток')
text_attempts.place(x=50, y=210)










window.mainloop()