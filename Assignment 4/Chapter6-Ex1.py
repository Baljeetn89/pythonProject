import random

def roll_dice():
    """Returns a random dice roll between 1 and 6."""
    return random.randint(1, 6)

def main():
    """Rolls the dice until the result is 6 and prints each roll."""
    roll = 0
    while roll != 6:
        roll = roll_dice()
        print(f"Rolled: {roll}")

if __name__ == "__main__":
    main()