def sum_of_digits (x):
    result = 0
    for i in str(x):
        result += int(i)
    return result

y = input("Enter a number: ")
print(sum_of_digits(y))