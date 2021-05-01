# Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

percent = int(input('Введите число от 0 до 20: '))

if percent == 1:
    print(percent, 'процент')
elif percent == 0 or percent <= 20:
    print(percent, 'процентов')
elif 2 <= percent <= 4:
    print(percent, 'процента')
else:
    print('Введенное число неверно')

print('-----------------------')
print('Выводим все склонения для проверки ')

for check in range(21):
    if check == 0 or check >= 5:
        print(check, 'процентов')
    elif check == 1:
        print(check, 'процент')
    elif check >= 2 or check <= 4:
        print(check, 'процента')
