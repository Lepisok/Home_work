from itertools import zip_longest
from json import dump, load
from sys import exit


def task_3():
    with open('users.csv', encoding='utf8') as fu, open('hobby.csv', encoding='utf8') as fh, open('dict.json', 'w', encoding='utf8') as fd:
        user_lines, hobby_lines = fu.readlines(), fh.readlines()
        if len(hobby_lines) > len(user_lines):
            return 1
        user_hobby_dict = {' '.join(k.strip().split(',')): v.strip().split(',') if v else None for k, v in zip_longest(user_lines, hobby_lines)}
        dump(user_hobby_dict, fd, ensure_ascii=False)
    with open('dict.json', encoding='utf8') as fd:
        check_dict = load(fd)
        print(check_dict)
    return 0


if __name__ == '__main__':
    exit(task_3())
