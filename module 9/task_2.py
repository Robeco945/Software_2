class Car:
    def __init__(self, registration_number, max_speed, c_speed = 0, travelled_distance = 0):
        self.c_speed = c_speed
        self.travelled_distance = travelled_distance
        self.registration_number = registration_number
        self.max_speed = max_speed

    def accelerate(self, speed):
        self.c_speed =  self.c_speed + speed
        if self.c_speed > self.max_speed:
            self.c_speed = self.max_speed
        elif self.c_speed < 0:
            self.c_speed = 0
        else:
            self.c_speed = self.c_speed

car = Car('ABC-123', 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f'{car.c_speed}km/h')

car.accelerate(-200)

print(f'{car.c_speed}km/h')

print(f'{car.registration_number}, {car.max_speed}km/h, {car.c_speed}km/h, {car.travelled_distance}km')
