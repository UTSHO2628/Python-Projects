import random

def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    guess = None
    attempts = 0

    print("Guess the number between 1 and 10")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")

    print(f"Congratulations! You've guessed the number in {attempts} attempts.")


number_guessing_game()
