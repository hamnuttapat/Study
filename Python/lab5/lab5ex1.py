print ("Pattern A")
data = eval(input("Enter number for pattern A and B: "))
for i in range (1, data + 1):
    for j in range (1, i+1):    
        print (j, end = " ")
    print()

print ("\nPattern B")
for i in range(data, 0, -1): 
    for j in range(1, i+1):  
        print(j, end=" ")
    print()