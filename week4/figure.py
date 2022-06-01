from turtle import *
l = 9
def draw_square():
    i = 0
    while i < 4:
        forward (30)
        right (90)
        i += 1
def paint():
    global l
    print(l)
    for n in range(l):
        if n < l-1:
            draw_square()
            left(90)
            forward(30)
            right(90)
        else:
            draw_square()
    if l >= 3:
        l = l - 2
        switch_row()
def switch_row():
    forward(30)
    right(90)
    forward(30*l)
    left(90)
    if l != 0:
        paint()
paint()
