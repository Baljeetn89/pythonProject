# Initialize an empty list to store city names
cities = []

# Use a for loop to ask the user for the names of five cities
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

# Print out the names of the cities, one per line
print("\nThe cities you entered are:")
for city in cities:
    print(city)