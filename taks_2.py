class Road:
    __length = None
    __width = None
    weigth = None
    thickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weigth = 25
        self.thickness = 0.05

    def building(self):
        building = self.length * self.width * self.weigth * self.thickness / 1000
        print("Итого: ", building, "тонн")


road = Road(20, 5000)
road.building()
