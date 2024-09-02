def inches_to_centimeters(inches):
    return inches * 2.54

def main():
    while True:
        try:
            inches = float(input("Enter the length in inches (negative value to quit): "))
            if inches < 0:
                print("Program terminated.")
                break
            centimeters = inches_to_centimeters(inches)
            print(f"{inches} inches is equal to {centimeters:.2f} centimeters.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()