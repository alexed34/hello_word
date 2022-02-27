import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm


def write_to_file(file_name):
    content = content_text.get(1.0, "end")
    with open(file_name, 'w') as file:
        file.write(content)

def open_file():
    global file_name
    file_name = tfd.askopenfilename()
    file_label["text"] = "Файл: " + file_name
    content_text.delete(1.0, "end")
    with open(file_name) as file:
        content_text.insert(1.0, file.read())
        file.read

def save_as_file():
    global file_name
    file_name = tk.filedialog.asksaveasfilename()
    file_label["text"] = "Файл: " + file_name
    write_to_file(file_name)

def save_file():
    global file_name
    if file_name == "":
        save_as_file()
    else:
        file_label["text"] = "Файл: " + file_name
        write_to_file(file_name)

def new_file():
    global file_name
    if tkm.askokcancel("Создание нового файла",
                       "Вы уверены? Несохраненный текст будет удален"):
        file_name = ""
        content_text.delete(1.0, "end")

window = tk.Tk()
window.title("Мой блокнот")
window.geometry("400x400")
file_name = ""
content_text = tk.Text(window, wrap="word")
content_text.place(x=0,y=0,relwidth=1, relheight=1)
main_menu = tk.Menu(window)

window.configure(menu=main_menu)
new_file_icon = tk.PhotoImage(file='img/new_file.gif')
open_file_icon =tk.PhotoImage(file="img/open_file.gif")
save_file_icon = tk.PhotoImage(file="img/save_file.gif")
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu2 = tk.Menu(main_menu, tearoff=0)

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Справка", menu=file_menu2)


file_menu.add_command(label="Новый файл", image=new_file_icon, compound="left", command = new_file)
file_menu.add_command(label="Открыть", image=open_file_icon, compound="left", command = open_file)
file_menu.add_command(label="Сохранить", image=save_file_icon, compound="left", command=save_file)
file_menu.add_command(label="Сохранить как", image=save_file_icon, compound="left", command=save_as_file)



file_label = tk.Label(window, text = "Файл: "+file_name)
file_label.place(relx=0, rely=1, anchor="sw")


window.mainloop()