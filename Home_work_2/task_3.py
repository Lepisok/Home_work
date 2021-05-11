position_and_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                     'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for element in position_and_name:
    greeting = 0 - element[::-1].find(' ')
    print(f'Привет, {element[greeting::].capitalize()}!')
