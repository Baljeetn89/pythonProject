# Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user.
TALENT_TO_POUNDS = 20
POUND_TO_LOTS = 32
LOT_TO_GRAMS = 13.3
GRAMS_TO_KG = 1000

# Ask user for input
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Convert the medieval units to grams
total_lots = (talents * TALENT_TO_POUNDS * POUND_TO_LOTS) + (pounds * POUND_TO_LOTS) + lots
total_grams = total_lots * LOT_TO_GRAMS

# Convert grams to kilograms and remaining grams
kilograms = int(total_grams // GRAMS_TO_KG)
grams = total_grams % GRAMS_TO_KG

# Output the result
print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")