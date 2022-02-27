import turtle

def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def circle():
    for i in range(60):
        t.forward(5)
        t.left(6)


def spiral():
    for i in range(160):
        t.forward(i/5)
        t.left(15)

def star():
    for i in range(5):
        t.forward(200)
        t.left(144)

def olympic_circle(x,y, color):
    t.color(color)
    t.width(10)
    move(x, y)
    circle()

def olympic_logo():
    olympic_circle(-120,60,"blue")
    olympic_circle(0, 60, "black")
    olympic_circle(120, 60, "red")
    olympic_circle(-60, 0, "yellow")
    olympic_circle(60, 0, "green")

def up():
    t.setheading(90)
    t.forward(10)

def down():
    t.setheading(-90)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

def up_or_down():
    if t.isdown():
        t.up()
    else:
        t.down()

t = turtle.Turtle()
t.speed(10)
t.screen.onkeypress(up,"Up")
t.screen.onkeypress(down, "Down")
t.screen.onkeypress(left, "Left")
t.screen.onkeypress(right,"Right")
t.screen.onkeypress(up_or_down, "space")
t.screen.listen()

t.screen.mainloop()