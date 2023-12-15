import turtle as t

n = eval(input("Enter number of rows and columns: "))
each = 100 / n

for b in range(n):
    for b in range(n):
        t.pendown()  
        for b in range(4):
            t.forward(each)
            t.left(90)
        t.penup()  
        t.forward(each)
    t.backward(each * n)
    t.left(90)  
    t.forward(each) 
    t.right(90)     
t.hideturtle()
t.done()