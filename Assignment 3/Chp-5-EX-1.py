import random

# Ask the user how many dice they want to roll
num_dice = int(input("How many dice would you like to roll? "))

# Initialize a variable to hold the sum of all dice rolls
total_sum = 0

# Roll the dice using a for loop
for i in range(num_dice):
    roll = random.randint(1, 6)  # Randomly generate a roll between 1 and 6
    print(f"Roll {i+1}: {roll}")  # Display each roll
    total_sum += roll  # Add the roll to the total sum

# Print the total sum of all the dice rolls
print(f"The total sum of the dice rolls is: {total_sum}")