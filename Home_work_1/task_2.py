# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

get_list = []

for numbers in range(1, 1001, 2):
    get_list.append(numbers ** 3)

print(get_list)

index = 0
addition = 0

for numbers_sum in get_list:
    result = 0
    new_number = numbers_sum
    while new_number > 0:
        result += new_number % 10
        new_number //= 10
        get_list[index] = result
    if (result % 7) == 0:
        addition += numbers_sum

print(addition)

index = 0
addition = 0

for numbers_sum in get_list:
    result = 0
    new_number = numbers_sum + 17
    while new_number > 0:
        result += new_number % 10
        new_number //= 10
        get_list[index] = result
    if (result % 7) == 0:
        addition += numbers_sum

print(addition)
