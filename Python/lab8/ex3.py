a = input("Enter a long string: ")
b = input("Enter a short string: ")
is_substring = False
for i in range(len(a) - len(b) + 1):
    if a[i:i + len(b)] == b:
        is_substring = True
        break
if is_substring:
    print("Short string is a substring of the long string")
else:
    print("Short string is not a substring of the long string")
