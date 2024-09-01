# Function to calculate the perimeter of the rectangle
def calculate_perimeter(length, width):
    return 2 * (length + width)

# Function to calculate the area of the rectangle
def calculate_area(length, width):
    return length * width

# Main function
def main():
    # Ask the user for the length and width of the rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the perimeter and area
    perimeter = calculate_perimeter(length, width)
    area = calculate_area(length, width)

    # Print the results
    print(f"The perimeter of the rectangle is: {perimeter}")
    print(f"The area of the rectangle is: {area}")

# Call the main function
if __name__ == "__main__":
    main()