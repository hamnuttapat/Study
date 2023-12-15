import math
sum = 0


for num in range (0, 5):
    num = int(input("Enter an integer: "))
    if num >= 0 and sum >= 0:
        sum += num
    elif num <= 0 and sum <=0:
        sum += num
    else:
        sum = num
    print("Current sum:\t ",sum)