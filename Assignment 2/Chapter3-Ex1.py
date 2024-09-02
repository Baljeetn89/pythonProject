def check_zander_length():
    # Ask for the length of the zander
    length = float(input("Enter the length of the zander in centimeters: "))

    # Size limit for zander
    size_limit = 42.0

    # Check if the zander meets the size limit
    if length >= size_limit:
        print("The zander meets the size limit. You can keep the fish.")
    else:
        # Calculate how many centimeters below the size limit the fish is
        below_limit = size_limit - length
        print(f"The zander does not meet the size limit. It is {below_limit:.2f} cm below the size limit.")
        print("Please release the fish back into the lake.")

# Call the function to execute the program
check_zander_length()