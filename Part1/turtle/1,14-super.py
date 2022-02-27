import turtle
wn = turtle.Screen()
wn.bgcolor('black')
s = turtle.Turtle()
s.speed('fastest')
s.color('white')
rotate = int(180)
def Circles(t, size):
    for i in range(10):
        t.circle(size)
        size -= 4

def design(t,size,repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360/repeat)


design(s, 200, 5)


s.screen.mainloop()