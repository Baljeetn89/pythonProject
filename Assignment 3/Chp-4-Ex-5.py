def login_system():
    # Correct username and password
    correct_username = "Baljeet"
    correct_password = "Kaur@baljeet"

    # Maximum number of attempts
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        # Ask the user for username and password
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if the credentials are correct
        if username == correct_username and password == correct_password:
            print("Welcome!")
            return  # Exit the function if login is successful

        # Increment the attempt counter
        attempts += 1
        print("Incorrect username or password. Try again.")

    # If the user reaches the maximum number of attempts
    print("Access denied.")


# Run the login system
login_system()