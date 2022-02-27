import tkinter

def add():
    num1 = int(text_num1.get())
    num2 = int(text_num2.get())
    set_answer(num2 + num1)

def sub():
    num1 = int(text_num1.get())
    num2 = int(text_num2.get())
    set_answer(num1 - num2)

def mul():
    num1 = int(text_num1.get())
    num2 = int(text_num2.get())
    set_answer(num2 * num1)

def div():
    num1 = int(text_num1.get())
    num2 = int(text_num2.get())
    set_answer(num1 / num2)

def set_answer(answer):
    text_answer.delete(0, "end")
    text_answer.insert(0, answer)

def get_button(text, command, x, y):
    button_add=tkinter.Button(window, text=text, command=command, width=3, height=2, bg="gold", )
    button_add.place(x=x, y=y)

window = tkinter.Tk()
window.configure(bg="silver")
window.title("Мой калькулятор")
window.geometry("300x300")

button_add = get_button('+', add, 95, 110)
button_sub = get_button('-', sub, 130, 110)





# button_add = tkinter.Button(window, text=" + ", command=add, width=3, height=2, bg = "gold" ,)
# button_add.place(x=95, y=110)
#
# button_sub = tkinter.Button(window, text=" - ", command=sub, width=3, height=2, bg = "gold")
# button_sub.place(x=130, y=110)

button_mul = tkinter.Button(window, text=" * ", command=mul, width=3, height=2, bg = "gold")
button_mul.place(x=165, y=110)

button_div = tkinter.Button(window, text=" / ", command=div, width=3, height=2, bg = "gold")
button_div.place(x=200, y=110)

text_num1 = tkinter.Entry(window, width=20)
text_num1.place(x=95, y=40)

text_num2 = tkinter.Entry(window, width=20)
text_num2.place(x=95, y=81)

text_answer = tkinter.Entry(window, width=20)
text_answer.place(x=95, y=221)

label_num1 = tkinter.Label(window, text="Введите первое число",bg="silver", fg = "red")
label_num1.place(x=95, y=20)

label_num2 = tkinter.Label(window, text="Введите второе число",bg="silver", fg = "red")
label_num2.place(x=95, y=61)

label_answer = tkinter.Label(window, text="Ответ",bg="silver", fg = "red")
label_answer.place(x=95, y=200)

window.mainloop()


