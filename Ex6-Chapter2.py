#Write a program that draws two random combinations of numbers for a combination lock:
import random
# Generate a 3-digit combination (each digit between 0 and 9)
def generate_3_digit_code():
    return [random.randint(0, 9) for _ in range(3)]

# Generate a 4-digit combination (each digit between 1 and 6)
def generate_4_digit_code():
    return [random.randint(1, 6) for _ in range(4)]

# Generate the codes
three_digit_code = generate_3_digit_code()
four_digit_code = generate_4_digit_code()

# Print the results
print("3-digit combination lock code:", three_digit_code)
print("4-digit combination lock code:", four_digit_code)