# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True

# Ask the user for an integer
user_input = int(input("Enter an integer: "))

# Check if the number is prime and print the result
if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")