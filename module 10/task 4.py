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


'''end = False
while not end:
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.drive(1)
        if car.dis_tra >= 10000:
            end = True
            break'''
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        count = 0
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            count += 1
            if count >= 10:
                count = 0
    def print_status(self):
        for car in self.cars:
            print(f' ______________________________    ______________     _________________')
            print(f'| registration number: {car.registration_number:<6s} |    | speed: {car.c_speed:3} |    | distance: {car.dis_tra:4} |')
    def race_finished(self):
        for car in self.cars:
            if car.dis_tra >= 8000:
                winner.append(car.registration_number)
                return True

for i in range(10):
    i += 1
    car = Car(f'ABC-{i}', random.randint(100,200))
    cars.append(car)
start = Race('Grand_Demolition_Derby', 8000, cars)
print(f"Let's begin the Grand Demolition Derby!!!\n")
count_2 = 0
end = False
while not end:
    start.hour_passes()
    count_2 += 1
    if count_2 >= 10:
        print(f'\n10 hours have passed,here are the status of the cars\n ')
        start.print_status()
        count_2 = 0
    start.race_finished()
    if start.race_finished():
        end = True
        print(f'\nThe race has ended, here are the results:\n')
        print(f'THE WINNER IS {winner[0]}')
        start.print_status()

    pass


