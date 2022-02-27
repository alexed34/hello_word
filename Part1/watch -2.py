from tkinter import *
import math
import datetime


def x_coordinate(length, angle):
    return width / 2 + length * math.cos(angle * math.pi / 180)


def y_coordinate(length, angle):
    return height / 2 - length * math.sin(angle * math.pi / 180)


width = 400
height = 400
radius = 150

root = Tk()
root.title("clock")

canvas = Canvas(root, width=width, height=height)
canvas.pack()

canvas.create_oval(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius)
seconds = canvas.create_line(0, 0, 0, 0, fill="red")
minutes = canvas.create_line(0, 0, 0, 0)
hours = canvas.create_line(0, 0, 0, 0)


def change_hand(length, time, clock_hand, degree):
    alpha = 90 - time * degree
    x1 = x_coordinate(0, alpha)
    y1 = x_coordinate(0, alpha)
    x2 = x_coordinate(length, alpha)
    y2 = y_coordinate(length, alpha)
    canvas.coords(clock_hand, x1, y1, x2, y2)


def update():
    time = str(datetime.datetime.now())
    #print(time, time[17:19])
    sec = int(time [17:19])
    min = int(time [14:15])
    h = int(time [11:12])


    change_hand(radius - 20, sec, seconds, 6)
    change_hand(radius - 60, min, minutes, 6)
    change_hand(radius / 2, h, hours, 30)

    root.after(1000, update)


alpha = 60
for i in range(1, 13):
    canvas.create_text(x_coordinate(radius + 10, alpha), y_coordinate(radius + 10, alpha), text=i, fill="darkblue",
                       font="Times 10 italic bold")
    alpha = alpha - 30

for i in range(60):
    x1 = x_coordinate(radius, alpha)
    y1 = y_coordinate(radius, alpha)

    if alpha % 30 == 0:
        x2 = x_coordinate(radius - 20, alpha)
        y2 = y_coordinate(radius - 20, alpha)
    else:
        x2 = x_coordinate(radius - 10, alpha)
        y2 = y_coordinate(radius - 10, alpha)
    canvas.create_line(x1, y1, x2, y2)
    alpha += 6

change_hand(200, 15, seconds, 6)

update()

root.mainloop()