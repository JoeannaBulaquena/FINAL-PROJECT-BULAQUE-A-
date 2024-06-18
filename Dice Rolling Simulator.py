import random

def dice_rolling_simulator():
    user_score, computer_score = 0, 0

    while user_score < 2 and computer_score < 2:
        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        print(f"You rolled: {user_roll}")
        print(f"Computer rolled: {computer_roll}")

        if user_roll > computer_roll:
            user_score += 1
            print("You win this round!")
        elif user_roll < computer_roll:
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

        print(f"Score - You: {user_score}, Computer: {computer_score}")

    if user_score == 2:
        print("Congratulations! You won the game.")
    else:
        print("Computer wins the game. Better luck next time.")

dice_rolling_simulator()