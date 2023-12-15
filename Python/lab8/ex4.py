first = input("Enter your first name: ")
last = input("Enter your last name: ")
gender = input("Enter your gender (m/f): ")
print(gender[0].upper() + last[0].upper() + first[0:7].upper())