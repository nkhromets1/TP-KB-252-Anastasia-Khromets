import random

user = input("Enter stone, scissor or paper: ")

computer = random.choice(["stone", "scissor", "paper"])

print("Your choice:", user)
print("Chossing a computer:", computer)

if user not in ["stone", "scissor", "paper"]:
    print("Incorrect value!")
elif user == computer:
    print("Draw!")
elif (user == "stone" and computer == "scissor") or \
     (user == "scissor" and computer == "paper") or \
     (user == "paper" and computer == "stone"):
    print("You won!")
else:
    print("The computer won!")