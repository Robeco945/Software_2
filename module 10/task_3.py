class Elevator:
    def __innit__(self,floor, top, bottom, name):
        self.top = top
        self.bottom = bottom
        self.floor = floor
        self.name = name
    def go_to_floor(self, floor):
        self.floor = floor
        print(f'moved to floor: {floor}')
    def floor_up(self):
        self.floor += 1
        print(f'moved to floor: {self.floor}')
    def floor_down(self):
        self.floor -= 1
        print(f'moved to floor: {self.floor}')

class Building:
    def __init__(self, top_floor, bottom_floor, noe):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.noe = noe
    def run_elevators(self, floor, noe):
        return
    def fire_alarm(self):
        self.go_to_floor(self.bottom_floor)
        print('A fire alarm has been pulled, moved all elevators to the bottom floor')


elevators =[]

for i in range(3):
    elevator = Elevator()
    elevators.append(elevator)

tower = Building(12, 1, 3)
tower.run_elevators(tower.top_floor, tower.bottom_floor)
tower.fire_alarm()
print(f'tower top floor: {tower.top_floor}, tower bottom floor: {tower.bottom_floor}, tower number of elevators: {tower.noe}')