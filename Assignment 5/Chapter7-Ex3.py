airport_data = {}

while True:
    print("\nOptions:")
    print("1. Add a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Select an option (1/2/3): ")

    if choice == '1':
        icao_code = input("Enter ICAO code: ").strip().upper()
        name = input("Enter airport name: ").strip()
        airport_data[icao_code] = name
        print(f"Added: {name} (ICAO: {icao_code})")

    elif choice == '2':
        icao_code = input("Enter ICAO code to fetch: ").strip().upper()
        if icao_code in airport_data:
            print(f"Airport Name: {airport_data[icao_code]}")
        else:
            print("Airport not found.")

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid option, please try again.")