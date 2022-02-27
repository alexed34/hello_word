import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm

def open_file():
    global file_name
    content_text.delete(1.0, 'end')
    file_name = tfd.askopenfilename()
    file_label["text"] = "Файл: " + file_name
    with open(file_name, 'r', encoding='utf8') as file:
        text = file.read()
        content_text.insert(1.0, text)

def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename(defaultextension = '.txt',filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    file_label["text"] = "Файл: " + file_name
    content = content_text.get(1.0, 'end')
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(content)

def save_file():
    global file_name
    if file_name == '':
        save_as_file()
    else:
        content = content_text.get(1.0, "end")
        with open(file_name, 'w', encoding='utf8') as file:
            file.write(content)
    file_label["text"] = "Файл: " + file_name

def new_file():
    global file_name
    if tkm.askokcancel("Создание нового файла", "Вы уверены? Несохраненный текст будет удален"):
        file_name = ""
        content_text.delete(1.0, "end")
    file_label["text"] = "Файл: " + file_name


windows = tk.Tk()
windows.title('Мой блокнот')
windows.geometry("400x400")
file_name = ""

content_text = tk.Text(windows, wrap='word')
content_text.place(x=0, y=0, relwidth=1, relheight=1)

main_nenu = tk.Menu(windows)
file_menu = tk.Menu(main_nenu, tearoff=0)
edit_menu = tk.Menu(main_nenu, tearoff=0)
format_menu = tk.Menu(main_nenu, tearoff=0)

windows.configure(menu=main_nenu)

main_nenu.add_cascade(label='Файл', menu=file_menu)
main_nenu.add_cascade(label='Правка', menu=edit_menu)
main_nenu.add_cascade(label='Формат', menu=format_menu)

new_file_ikon = tk.PhotoImage(file='img/new_file.gif')
open_file_ikon = tk.PhotoImage(file='img/open_file.gif')
save_file_ikon = tk.PhotoImage(file='img/save_file.gif')

file_menu.add_command(label='Новый', image=new_file_ikon, compound='left', command=new_file)
file_menu.add_command(label='Открыть', image=open_file_ikon, compound='left', command=open_file)
file_menu.add_command(label='Сохранит', image=save_file_ikon, compound='left', command=save_file)
file_menu.add_command(label='Сохранит как', image=save_file_ikon, compound='left', command=save_as_file)


file_label = tk.Label(windows, text = "Файл: "+file_name)
file_label.place(relx=0, rely=1, anchor="sw")













windows.mainloop()



