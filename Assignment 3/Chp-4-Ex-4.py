import random


def guessing_game():
    # Computer selects a random number between 1 and 10
    number_to_guess = random.randint(1, 10)

    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            # Ask the user to input their guess
            guess = int(input("Enter your guess: "))

            # Compare the guess to the number
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Correct! You've guessed the number!")
                break  # Exit the loop if the guess is correct

        except ValueError:
            print("Please enter a valid integer.")


# Run the game
guessing_game()