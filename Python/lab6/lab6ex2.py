
def main():
    xxx = eval(input("Enter X for each square side: "))
    square(xxx)


def square(x):
    r = 8   
    import turtle as t
    for i in range(4):
            for i2 in range(4):
                t.speed(0)
                t.pd()
                t.forward(r*x)
                t.left(90)
                t.forward(r*x)
                t.left(90)
                t.forward(r*x)
                t.left(90)
                t.forward(r*x)
            r -= 2                                                           
    t.ht()
    t.done()
main()
