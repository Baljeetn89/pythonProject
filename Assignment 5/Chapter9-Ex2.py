class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number  # Registration number
        self.max_speed = max_speed  # Maximum speed
        self.current_speed = 0  # Current speed (initialized to 0)
        self.travelled_distance = 0  # Travelled distance (initialized to 0)

    def accelerate(self, change):
        # Calculate new speed
        new_speed = self.current_speed + change

        # Ensure speed is within limits
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed  # Set to max speed if exceeding
        elif new_speed < 0:
            self.current_speed = 0  # Set to 0 if speed is negative
        else:
            self.current_speed = new_speed  # Set to new speed if valid


# Main program
if __name__ == "__main__":
    # Create a new car
    my_car = Car("PB-155", 150)

    # Increase speed
    my_car.accelerate(30)  # Increase by 30 km/h
    my_car.accelerate(70)  # Increase by 70 km/h
    my_car.accelerate(50)  # Attempt to increase by 50 km/h

    # Print current speed after accelerations
    print("Current Speed after accelerations:", my_car.current_speed, "km/h")

    # Use emergency brake
    my_car.accelerate(-200)  # Attempt to decrease speed by 200 km/h

    # Print final speed
    print("Final Speed after emergency brake:", my_car.current_speed, "km/h")
