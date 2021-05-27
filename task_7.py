from sys import argv, exit


def write_data(*args):
    if len(args) != 2:
        print('Неверно указана сумма.')
        return 1
    with open('bakery.csv', 'a', encoding='utf8') as f:
        s = f'\n{args[1]}' if f.tell() != 0 else args[1]  # если файл новый - пишем без \n
        f.write(s)
    return 0


if __name__ == '__main__':
    exit(write_data(*argv))