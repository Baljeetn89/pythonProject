class Car:
    def __init__(self, initial_distance=0, speed=0):
        self.traveled_distance = initial_distance  # in kilometers
        self.speed = speed  # in kilometers per hour

    def drive(self, hours):
        # Calculate the distance traveled in the given time
        distance_traveled = self.speed * hours
        # Increase the traveled distance
        self.traveled_distance += distance_traveled

    def __str__(self):
        return f"Traveled Distance: {self.traveled_distance} km, Current Speed: {self.speed} km/h"

# Example usage
car = Car(initial_distance=4000, speed=80)  # Initial distance 4000 km, speed 80 km/h
print(car)

# Drive for 1.5 hours
car.drive(1.5)
print(car)
