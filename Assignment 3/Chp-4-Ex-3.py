def find_min_max():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to quit): ")

        # Break the loop if the input is an empty string
        if user_input == "":
            break

        try:
            # Convert input to a float (to handle decimals) or int
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("That's not a valid number. Please try again.")

    if numbers:
        print(f"Smallest number: {min(numbers)}")
        print(f"Largest number: {max(numbers)}")
    else:
        print("No numbers were entered.")

# Run the function
find_min_max()