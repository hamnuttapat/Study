import turtle as t

n = eval(input("Enter number of rows and columns: "))
each = 100 / n

colors = ["black", "white"] 

for i in range(n):
    for j in range(n):
        color_index = (i + j) % 2 
        t.fillcolor(colors[color_index])  
        t.begin_fill()  
        t.pendown()  
        for _ in range(4):
            t.forward(each)
            t.left(90)
        t.penup()  
        t.forward(each)
        t.end_fill() 
    t.backward(each * n)  
    t.left(90)  
    t.forward(each) 
    t.right(90) 
t.hideturtle()
t.done()