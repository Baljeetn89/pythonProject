# Initialize an empty list to store the user's numbers
numbers = []

# Ask the user to enter numbers until they input an empty string
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":  # Break the loop if the input is empty
        break

    try:
        # Convert input to a number and add it to the list
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

# Sort the numbers in descending order and get the top 5
numbers.sort(reverse=True)
top_five = numbers[:5]

# Print the five greatest numbers
print(f"The five greatest numbers are: {top_five}")