import random
cars = []
winner = []
class Car:
    def __init__(self, registration_number, max_speed, c_speed = 0, dis_tra = 0):
        self.c_speed = c_speed
        self.dis_tra = dis_tra
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

    def drive(self, hours):
        self.dis_tra += self.c_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, bat_capacity):
        super().__init__(registration_number, max_speed)

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_capacity):
        super().__init__(registration_number, max_speed)


cars = []
cars.append(ElectricCar('ABC-15', 180, 52.5))
cars.append(GasolineCar('ACD-123', 165, 32.3))

for c in cars:
    c.accelerate(150)
    c.drive(3)
    print(f'car: {c.registration_number} ,distant traveled: {c.dis_tra}')
