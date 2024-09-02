def is_leap_year(year):
    """Check if a year is a leap year."""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def main():
    """Main function to ask the user for a year and check if it's a leap year."""
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()
