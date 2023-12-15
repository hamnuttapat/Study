import turtle as t

def draw_polygon(x, y, side = 4, size = 100):
    t.pu()
    t.goto(x,y)
    t.pd()
    for i in range(side):
        t.forward(size)
        t.left(360/side)
draw_polygon(10,10,5)
t.done()