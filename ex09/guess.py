import random

def guessing_game():
    secret_number = random.randint(1, 99)
    num_trials = 0

    while True:
        guess = input("Guess a number between 1 and 99 (or type 'exit' to quit): ")

        if guess.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid.Enter a number or 'exit'.")

        num_trials += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("You found the secret number in", num_trials, "trials.")