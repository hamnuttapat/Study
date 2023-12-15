character = str(input("Please enter a character: "))

if len(character) == 1:
    ascii = ord(character) 
    if 97 <= ascii <= 122:
        ord = ascii-32
        newcharacter = chr(ord)
        print(character, "is a small-case letter and its capital letter is ", newcharacter,"\b.")
    if 65 <= ascii <= 90:
        ord2 = ascii+32
        newcharacter2 = chr(ord2)
        print(character, "is a capital letter and its small-case letter is ",newcharacter2,"\b.")
    if 48 <= ascii <= 57:
        print(character, "is a numeric character.")

    if 1 <= ascii <= 47:
        print("Special character")    
    if 58 <= ascii <= 64:
        print("Special character")
    if 123 <= ascii:
        print("Special character")
else:
    print("Wrong length")
    






