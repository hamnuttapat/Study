score = int(input("Enter a score "))
if 0 <= score <= 100:
    if 80 <= score <= 100:
        print ("Your grade : A") 

    if 70 <= score < 80:
        print ("Your grade : B")

    if 60 <= score < 70:
        print ("Your grade : C")

    if 50 <= score < 60:
        print ("Your grade : D")

    if score < 50:
        print ("Your grade : F")
else:
    print("Error")