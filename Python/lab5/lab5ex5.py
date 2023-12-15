while True:
    c=input("Please enter a character: ")

    if len(c) != 1:
        print("Please enter exactly one character.")
        continue
    if c=="\t":
        print("Good bye, see you tomorrow.")
        break
    elif ord(c)>=0x30 and ord(c)<=0x39:
        print(c,"is a numeric character.")
    elif ord(c)>=0x41 and ord(c)<=0x5A:
        print(c,"is a capital letter and its small-case letter is", c.lower())
    elif ord(c)>=0x61 and ord(c)<=0x7A:
        print(c,"is a small-case letter and its capital letter is", c.upper())
    else:
        print(c,"is a special letter.")