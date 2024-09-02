import math


def calculate_unit_price(diameter_cm, price_euros):
    """Calculates the unit price of pizza per square meter."""
    # Convert diameter from cm to meters
    diameter_m = diameter_cm / 100
    # Calculate the radius in meters
    radius_m = diameter_m / 2
    # Calculate the area in square meters
    area_m2 = math.pi * (radius_m ** 2)
    # Calculate the unit price (price per square meter)
    unit_price_per_m2 = price_euros / area_m2
    return unit_price_per_m2


def main():
    """Compares the value for money between two pizzas based on user input."""
    print("Enter details for the first pizza:")
    diameter1 = float(input("Diameter in centimeters: "))
    price1 = float(input("Price in euros: "))

    print("Enter details for the second pizza:")
    diameter2 = float(input("Diameter in centimeters: "))
    price2 = float(input("Price in euros: "))

    # Calculate unit prices
    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    print(f"\nPizza 1 unit price: {unit_price1:.2f} euros per square meter")
    print(f"Pizza 2 unit price: {unit_price2:.2f} euros per square meter")

    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price1 > unit_price2:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same value for money.")


if __name__ == "__main__":
    main()