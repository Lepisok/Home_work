class Date:
    def __init__(self, date_str):
        self.date_tuple = Date.__str_to_int(date_str)

    def __str__(self):
        return '{}-ое {} {} года'.format(*self.date_tuple)

    @classmethod
    def __str_to_int(cls, date_str):
        try:
            num = int(date_str[:2])
            month = int(date_str[2:4])
            year = int(date_str[4:])
        except ValueError:
            print('Error enter date')

        return Date.__chek_date(num, month, year)

    @staticmethod
    def __chek_date(num, month, year):
        if 12 < month or month < 0:
            print('Error month')
        if 31 < num or num < 0:
            print('Error number date')
        if year < 21:
            year += 2001
        elif year < 100:
            year += 1900
        return (num, month, year)

if __name__ == '__main__':
    d = Date('040720')
    print(d)
