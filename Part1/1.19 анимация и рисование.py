import tkinter as tk
import random
import time


def draw_circle():
    color = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(0, 500 - d)
    y = random.randint(0, 500 - d)
    canvas.create_oval(x, y, x + d, y + d, fill=color)


def draw_oval():
    color = random.choice(colors)
    d1 = random.randint(1, 100)
    d2 = random.randint(1, 100)
    x = random.randint(0, 500 - d1)
    y = random.randint(0, 500 - d2)
    canvas.create_oval(x, y, x + d1, y + d2, fill=color)


def draw_square():
    color = random.choice(colors)
    color_border = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(0, 500 - d)
    y = random.randint(0, 500 - d)
    canvas.create_rectangle(x, y, x + d, y + d, fill=color, outline=color_border)


def draw_circles():
    global stop
    while True:
        draw_circle()
        time.sleep(1)
        window.update()
        if stop:
            stop = False
            break


def stop_draw():
    global stop
    stop = True


def animate_circle():
    global stop
    # global coords_paddle
    color = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(0, 500 - d)
    y = random.randint(0, 500 - d)
    circle = canvas.create_oval(x, y, x + d, y + d, fill=color)
    dx = 2
    dy = 3
    while True:
        coords = canvas.coords(circle)
        left = coords[0]
        top = coords[1]
        right = coords[2]
        bottom = coords[3]

        left_padle = coords_paddle[0]
        top_padle = coords_paddle[1]
        right_padle = coords_paddle[2]
        bottom_padle = coords_paddle[3]
        # print(left_padle)
        print(coords_paddle, coords)
        bottom_ball = left + (right - left) / 2

        if bottom_ball > left_padle and bottom_ball < right_padle and bottom >= 480:
            dy = -dy

        if left <= 0 or right >= 500:
            dx = -dx
        if top <= 0 or bottom >= 500:
            dy = -dy

        canvas.move(circle, dx, dy)
        time.sleep(0.001)
        window.update()
        if stop:
            stop = False
            canvas.delete(circle)
            break


def move_paddle_right(event):
    global padl
    global coords_paddle
    coords_paddle = canvas.coords(padl)
    print(coords_paddle)
    right = coords_paddle[2]
    if right < 500:
        canvas.move(padl, 5, 0)


def move_paddle_lift(event):
    global padl
    global coords_paddle
    coords_paddle = canvas.coords(padl)
    print(coords_paddle)
    left = coords_paddle[0]
    if left > 0:
        canvas.move(padl, -5, 0)


window = tk.Tk()
window.geometry("650x500")
window.title("Цветные фигуры")
canvas = tk.Canvas(window, bg="white", width=500, height=500)
canvas.place(x=0, y=0)
colors = ['red', 'blue', 'green', 'pink', 'black', 'yellow', 'orange', 'purple', 'brown']
stop = False
coords_paddle = [10.0, 480.0, 110.0, 490.0]

button_circle = tk.Button(window, width=17, text="Нарисовать круг", command=draw_circle)
button_circle.place(x=510, y=20)

button_oval = tk.Button(window, width=17, text="Нарисовать овал", command=draw_oval)
button_oval.place(x=510, y=90)

button_square = tk.Button(window, text="Нарисовать квадрат", width=17, command=draw_square)
button_square.place(x=510, y=150)

button_circles = tk.Button(window, text="Бесконечные круги", width=17, command=draw_circles)
button_circles.place(x=510, y=220)

stop_button = tk.Button(window, text="Остановить анимацию", bg="orange", width=17, command=stop_draw)
stop_button.place(x=510, y=360)

button_circle_a = tk.Button(window, text="Анимировать круг", width=17, command=animate_circle)
button_circle_a.place(x=510, y=290)

padl = canvas.create_rectangle(10, 480, 110, 490, fill='green')
window.bind("<Right>", move_paddle_right)
window.bind("<Left>", move_paddle_lift)

window.mainloop()
