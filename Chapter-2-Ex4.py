# Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate the sum
sum_of_numbers = num1 + num2 + num3

# Calculate the product
product_of_numbers = num1 * num2 * num3

# Calculate the average
average_of_numbers = sum_of_numbers / 3

# Print the results
print(f"\nSum of the numbers: {sum_of_numbers}")
print(f"Product of the numbers: {product_of_numbers}")
print(f"Average of the numbers: {average_of_numbers:.2f}")