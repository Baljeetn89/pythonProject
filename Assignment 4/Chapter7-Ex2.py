def main():
    """Reads names from the user, identifies new and existing names, and lists all unique names."""
    names_set = set()  # Create a set to store unique names

    while True:
        name = input("Enter a name (or press Enter to finish): ").strip()

        if name == "":
            break  # Exit the loop if the input is an empty string

        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)  # Add the new name to the set

    print("\nList of names entered:")
    for name in names_set:
        print(name)


if __name__ == "__main__":
    main()