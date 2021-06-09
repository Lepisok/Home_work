class Car:
    speed = None
    color = None
    name = None

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print("Машина повернула ", direction)

    def show_speed(self):
        print("Текущая скорость атомобиля: ", self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Для TownCar превышение скорости")
        else:
            print("Для TownCar скорость в пределах нормы")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Для WorkCar превышение скорости")
        else:
            print("Для WorkCar скорость в пределах нормы")


my_car = Car(71, "red", "Ferrari")
print(my_car.go(), my_car.stop(), my_car.turn("куда-то"), my_car.show_speed())
my_town_car = TownCar(51, "red", "Ferrari")
my_town_car.show_speed()
my_work_car = WorkCar(51, "red", "Ferrari")
my_work_car.show_speed()
