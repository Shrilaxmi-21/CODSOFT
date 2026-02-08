import random
print("     ROCK PAPER SCISSORS GAME")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:

    print("\nChoose one:")
    print("Rock")
    print("Paper")
    print("Scissors")

    user_choice = input("\nEnter your choice: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please select rock, paper, or scissors.")
        continue
    computer_choice = random.choice(choices)

    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)
    if user_choice == computer_choice:
        print("It's a Tie!")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You Win!")
        user_score += 1

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You Win!")
        user_score += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1
    print("\nCurrent Scores:")
    print("You:", user_score)
    print("Computer:", computer_score)

    again = input("\nDo you want to play again? (y/n): ")

    if again.lower() != 'y':
        print("\nFinal Scores:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("\nThank you for playing!")
        break