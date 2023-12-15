number = str(input("Enter a number "))

try:
    number2 = int(number)
    number3 = int(number2)
    number4 = str(input("binary, octal, hexidecimal, or decimal format: "))
    if number4 == "binary":
        bin2 = bin(number2)
        print (bin2)
    if number4 == "octal":
        ooc = oct(number2)
        print(ooc)
    if number4 == "hexadecimal":
        hex2 = hex(number2)
        print (hex2)  
    if number4 == "decimal format":
        print(number2)
except ValueError: 
    number = float(number)
    num = float(number)
    types = str(input("Display the number in a floating point or sciencetific format: "))
    if types == "floating point":
        num = float(number)
        print (float(num))
    if types == "sciencetific format":
        print (f"{number:e}")
