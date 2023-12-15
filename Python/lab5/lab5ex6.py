inpt = int(input("Enter number of line:"))
a = int(inpt/2)
b = inpt - a


for num in range(0, a+1):
    for x in range(num-1, -1, -1):
        print(2**x, end=" ")
    print()

for num in range(b - 1, 0, -1):
    for x in range(num, -1, -1):
        print(2**x, end=" ")
    print()
print(1)