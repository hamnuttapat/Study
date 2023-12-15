def grade(score):
    if score < 0 or score > 100:
        return("Invalid score")
        
    elif score >= 90:
        return('A')
    elif score >= 80:
        return('B')
    elif score >= 70:
        return('C')
    elif score >= 60:
        return('D')
    else:
        return('F')

def main():
    score = eval(input("Enter a score: "))
    print("The grade is", grade(score))

main()