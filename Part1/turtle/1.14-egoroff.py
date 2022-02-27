import turtle
def sq(a):
    for i in range(4):
        joe.color(colors[i%4])
        joe.forward(a)
        joe.left(90)

colors = ['red', 'blue', 'green', 'brown']


joe = turtle.Turtle()
joe.speed(100)

dlina = 30
for i in range(60):
    #sq(dlina)
    joe.circle(dlina)
    joe.color(colors[i % 4])
    print(i % 4, i)
    joe.right(10)
    dlina+= 4



joe.screen.mainloop()