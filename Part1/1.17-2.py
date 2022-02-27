import tkinter
import tkinter.messagebox as tmb
import random


def new_word():
    color_label['fg'] = random.choice(colors)
    color_label['text'] = random.choice(colors)


def check(event):
    print('Проверка')
    global score
    global fails
    if times > 0:
        user_color = entry.get()  # введеный цвет
        word_color = color_label['fg']  # цвет слова
        if user_color == word_color:
            print('yes')
            score += 1
            score_label['text'] = f'Правильно {score}'
        else:
            print('no')
            fails += 1
            fails_label['text'] = f'Неправильно {fails}'



    new_word()
    entry.delete(0, 'end')  # очищаем поле


def timer():
    global times
    global score
    global fails
    if times > 0:
        times -= 1
        time_label['text'] = f'Осталось секунд {times}'
        time_label.after(1000, timer)
    else:
        tmb.showinfo('Конец игры', 'Время вышло')
        if score > fails:
            tmb.showinfo('результат','Хороший результат, Ты молодец.')
        else:
            tmb.showinfo("Неважный результат", "В следующий раз получится лучше")
        # new_word()
        # times = 5
        # score = 0
        # fails = 0



windows = tkinter.Tk()
windows.title('Назови цвет')
windows.geometry('350x250')

colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "purple", \
          "brown", "white"]

score = 0  # скоо
fails = 0  # фээилс
times = 5

instructions = tkinter.Label(windows, text='Введите цвет слова, а не слово!\
 \n Жми Enter, чтобы играть.', font=('Helvetica', 10))
instructions.place(x=10, y=10)

color_label = tkinter.Label(windows, text='color', font=('Helvetica', 60))
color_label.place(x=10, y=80)

entry = tkinter.Entry(windows, font=('Helvetica', 10))
entry.place(x=10, y=180)
entry.focus_set()  # курсор сразу устанавливается в поле

score_label = tkinter.Label(windows, text=f'Правильно: {score}', font=("Helvetica", 10))
score_label.place(x=10, y=50)

fails_label = tkinter.Label(windows, text=f'Неправильно: {fails}', font=("Helvetica", 10))
fails_label.place(x=10, y=70)

time_label = tkinter.Label(windows, text=f'Осталось секунд {times}')
time_label.place(x=10, y=210)

new_word()
windows.bind('<Return>', check)  # Return это Enter
#timer()
time_label.after(1000, timer)

windows.mainloop()
