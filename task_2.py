from abc import ABC, abstractmethod

class dress(ABC):

    @abstractmethod
    def sum_cloth(self):
        pass

class coat(dress):
    def __init__(self, v :float):
        self.v = v

    @property
    def sum_cloth(self):
        answer = self.v / 6.5 + 0.5
        return round(answer, 3)

class suit(dress):
    def __init__(self, h :float):
        self.h = h

    @property
    def sum_cloth(self):
        answer = self.h * 2 + 0.3
        return answer