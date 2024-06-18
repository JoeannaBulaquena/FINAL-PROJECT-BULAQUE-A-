import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed it!")
            break

number_guessing_game()