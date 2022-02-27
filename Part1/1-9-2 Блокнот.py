""""
main_nenu -главное
file_menu, edit_menu, format_menu - подменю


"""



import tkinter


windows = tkinter.Tk()
windows.title('Мой блокнот')
windows.geometry('400x400')

new_file_ikon = tkinter.PhotoImage(file='img/new_file.gif')
open_file_ikon = tkinter.PhotoImage(file='img/open_file.gif')
save_file_ikon = tkinter.PhotoImage(file='img/save_file.gif')



content_text = tkinter.Text(windows, wrap='word')
content_text.place(x=0, y=0, relwidth=1, relheight=1)

main_nenu = tkinter.Menu(windows)
windows.configure(menu=main_nenu)

file_menu = tkinter.Menu(main_nenu, tearoff=0)
edit_menu = tkinter.Menu(main_nenu, tearoff=0)
format_menu = tkinter.Menu(main_nenu, tearoff=0)

main_nenu.add_cascade(label='Файл', menu=file_menu)
main_nenu.add_cascade(label='Правка', menu=edit_menu)
main_nenu.add_cascade(label='Формат', menu=format_menu)



file_menu.add_command(label='Новый', image=new_file_ikon,  compound='left', )
file_menu.add_command(label='Открыть', image=open_file_ikon,  compound='left', )
file_menu.add_command(label='Сохранить', image=save_file_ikon,  compound='left', )
file_menu.add_command(label='Сохранит как', image=save_file_ikon,  compound='left', )

















windows.mainloop()