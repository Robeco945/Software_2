class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

car = Car('ABC-123', '142km/h')

print(f'{car.registration_number}, {car.maximum_speed}km/h, {car.current_speed}km/h, {car.travelled_distance}km ')