import random
cars = []


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


for i in range(10):
    i += 1
    car = Car(f'ABC-{i}', random.randint(100,200))
    cars.append(car)
end = False
while not end:
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.drive(1)
        if car.dis_tra >= 10000:
            end = True
            break
for car in cars:
    print(f'registration number: {car.registration_number}  speed: {car.c_speed}  distance: {car.dis_tra}')



#for car in cars:
 #   print(car.registration_number, car.c_speed, car.dis_tra)


