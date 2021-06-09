class Stationery:
    title = None

    def draw(self):
        print("1) Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("2) Отрисовка запущена.")


class Pencil(Stationery):
    def draw(self):
        print("3) В процессе отрисовки.")


class Handle(Stationery):
    def draw(self):
        print("4) Отрисовка завершена.")


my_stationery = Stationery()
my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
