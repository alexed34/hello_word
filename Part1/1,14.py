import turtle
def square():
    for i in range(4):
        t.forward(100)
        t.left(90)

def move(x,y):
    t.up()
    t.goto(x, y)
    t.down()

def pentagon():
    for i in range(5):
        t.forward(100)
        t.left(72)

def polygon(sides):
    for i in range(sides):
        t.forward(50)
        t.left(360/sides)

t = turtle.Turtle()
#t.shape("turtle")
t.speed(100)
square()
move(100,100)
pentagon()
move(150,150)
polygon(6)
move(-150,150)

polygon(9)
move(-150,-150)
polygon(12)
for i in range(60):
    t.forward(20)
    t.left(6)

t.screen.mainloop()