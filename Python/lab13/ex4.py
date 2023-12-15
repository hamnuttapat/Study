import turtle as t

def cross(n, length):
    t.speed(0)
    if n > 0:
        for i in range(4):
            t.fd(length)
            
            cross(n-1, length // 2)
            t.back(length)
            t.lt(90)
    else:
        t.dot(5)

cross(4,100)
t.exitonclick()