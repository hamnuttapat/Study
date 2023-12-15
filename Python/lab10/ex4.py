import turtle as t
list = [1,2,2,1,3,4,6,5,3,4,5,6,4,3,5,4,5,3,4,4,3,3,4,3,3,4,4,4,10]
maxvalue = max(list)
minvalue = min(list)
for i in range(minvalue,maxvalue+1):
    a = list.count(i)
    if a!=0:
        t.left(90)
        t.pu()
        t.backward(20)
        t.write(i)
        t.forward(20)
        t.pd()
        t.forward(10*a)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(10*a)
        t.right(90)
        t.forward(10)
        t.right(180)
        t.forward(10)
        
    else:
        continue

t.done()
    


