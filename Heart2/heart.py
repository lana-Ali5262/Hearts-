import turtle

wn = turtle.Screen()
wn.bgcolor('black')
t = turtle.Turtle()
t.speed(0)

def curve():

    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    # minimal placeholder heart setup (replace with your drawing code)
    t.color('red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()
    t.hideturtle()


heart()

def write(message, pos):
    x,y = pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    style=('Stencil std', 18, 'italic')
    t.write(message,font = style)

write('I', (-68,95))
write('L', (-55,95))
write('O', (-42,95))
write('V', (-28,95))
write('E', (-14,95))
write('Y', (10,95))
write('O', (26,95))
write('E', (45,95))

wn.mainloop()