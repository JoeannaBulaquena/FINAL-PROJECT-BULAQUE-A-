import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_score, computer_score = 0, 0

    while user_score < 2 and computer_score < 2:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")

        print(f"Score - You: {user_score}, Computer: {computer_score}")

    if user_score == 2:
        print("Congratulations! You won the game.")
    else:
        print("Computer wins the game. Better luck next time.")

rock_paper_scissors()