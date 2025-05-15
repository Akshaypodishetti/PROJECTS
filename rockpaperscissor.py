import random
rock = 0
paper = 1
scissor = 2
game = [rock,paper,scissor]
user_input = int(input("Enter your input [(rock = 0),(paper = 1),(scissor = 2)]:"))
if user_input >= 3 or user_input < 0:
    print("you entered invalid number, you lose.")
else:
    computer_input = random.randint(0,2)
    print("computer_input:")
    print(computer_input)
    if computer_input == user_input:
        print("Its a draw match")
    elif computer_input == 0 and user_input == 2:
        print("you won the match")
    elif user_input == 0 and computer_input == 2:
        print("you lost the match")
    elif computer_input > user_input:
        print("you lost the match")
    elif user_input > computer_input:
        print("you won the match")
