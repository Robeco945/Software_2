class Elevator:
    def __innit__(self,floor, top, bottom):
        self.top = top
        self.bottom = bottom
        self.floor = floor

    def go_to_floor(self, floor):
        self.floor = floor
        print(f'moved to floor: {floor}')
    def floor_up(self):
        self.floor += 1
        print(f'moved to floor: {self.floor}')

    def floor_down(self):
        self.floor -= 1
        print(f'moved to floor: {self.floor}')

h = Elevator()

h.go_to_floor(5)
h.floor_up()
h.go_to_floor(6)

