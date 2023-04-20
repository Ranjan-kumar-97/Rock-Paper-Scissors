import random

user_wins=0
compurt_wins=0
tie=0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit:  ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Invalid choice")
        continue

    random_number = random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + " . ")

    if user_input == "rock" and computer_pick == "scissors":
        print("Your Won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("Your Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("Your Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "scissors" or user_input == "paper" and computer_pick == "paper" or user_input == "rock" and computer_pick == "rock":
        print("Match Tie!")
        tie += 1

    else:
        print("You Lost!")
        compurt_wins += 1


        
print("You won", user_wins, "times.")
print("Computer won", compurt_wins, "times.")
print("Match Ties", tie, "times.")
print("See You Again!\n")