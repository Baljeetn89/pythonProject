def get_season(month):
    """Returns the season corresponding to the given month number."""
    # Define the seasons in a tuple, where each index corresponds to a season
    seasons = ("Winter", "Spring", "Summer", "Autumn")

    # Map month numbers to seasons
    if month in {12, 1, 2}:  # December, January, February
        return seasons[0]
    elif month in {3, 4, 5}:  # March, April, May
        return seasons[1]
    elif month in {6, 7, 8}:  # June, July, August
        return seasons[2]
    elif month in {9, 10, 11}:  # September, October, November
        return seasons[3]
    else:
        return "Invalid month number"


def main():
    """Asks the user for a month number and prints the corresponding season."""
    try:
        month = int(input("Enter the number of the month (1-12): "))
        season = get_season(month)
        if season == "Invalid month number":
            print(season)
        else:
            print(f"The season for month {month} is {season}.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 12.")


if __name__ == "__main__":
    main()