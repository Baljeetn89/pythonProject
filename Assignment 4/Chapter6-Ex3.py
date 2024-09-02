def gallons_to_liters(gallons):
    """Converts gallons to liters."""
    # 1 gallon is approximately 3.78541 liters
    liters_per_gallon = 3.78541
    return gallons * liters_per_gallon

def main():
    """Asks the user for a volume in gallons and converts it to liters."""
    while True:
        try:
            gallons = float(input("Enter the volume in gallons (or a negative value to quit): "))
            if gallons < 0:
                print("Negative value entered. Exiting.")
                break
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is approximately {liters:.2f} liters.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()