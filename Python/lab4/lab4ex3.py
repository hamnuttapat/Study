import random
user = str(input("Enter number for scissor-rock-paper game\nscissor (0), rock(1), paper(2): "))
bot = random.randint(0,2)
if bot == 0 and user == "0":
 print ("The computer is scissor. You are scissor. It is a draw")
if bot == 0 and user == "1":
 print ("The computer is scissor. You are rock. You win")
if bot == 0 and user == "2":
 print ("The computer is scissor. You are paper. You lose")
if bot == 1 and user == "0":
 print ("The computer is rock. You are scissor. You lose")
if bot == 1 and user == "1":
 print ("The computer is rock. You are rock. It is a draw")
if bot == 1 and user == "2":
 print ("The computer is rock. You are paper. You win")
if bot == 2 and user == "0":
 print ("The computer is paper. You are scissor. You win")
if bot == 2 and user == "1":
 print ("The computer is paper. You are rock. You lose")
if bot == 2 and user == "2":
 print ("The computer is paper. You are paper. It is a draw")
 