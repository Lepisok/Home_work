class Worker:
    name = None
    surname = None
    position = None
    income = None

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income


class Position (Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self.income


manager = Position("Сергей ", "Сергеев", 'engineer', 43242)
print(manager.get_full_name(), manager.get_total_income())
