class Complex:
    def __init__(self, number, inumber):
        self.complex = complex(number, inumber)

    def __add__(self, other):
        return self.complex + other.complex

    def __mul__(self, other):
        return self.complex * other.complex


if __name__ == '__main__':
    one = Complex(1, 2)
    two = Complex(3, 4)
    print(one + two)
    print(one * one)
