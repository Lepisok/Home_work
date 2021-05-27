from sys import exit


def task_4():
    with open('users.csv', encoding='utf8') as fu, open('hobby.csv', encoding='utf8') as fh, open('users_hobby.txt', 'w', encoding='utf8') as fd:
        for user_line in fu:
            hobby_line = fh.readline().strip()  # strip для контроля за \n
            fd.write(f'{user_line.strip()}: {hobby_line if hobby_line else None}\n')
        if fh.readline():
            return 1
    return 0


if __name__ == '__main__':
    exit(task_4())