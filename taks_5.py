import os
from collections import defaultdict
from json import dump

file_size_cnt = defaultdict(lambda: [0, set()])
file_size_cnt_dict = dict()


def get_size_for_dict(n):
    if not n:
        return 0
    cnt = 1
    while True:
        dict_size = 10 ** cnt
        if n < dict_size:
            return dict_size
        else:
            cnt += 1


for r, d, f in os.walk(os.getcwd()):
    with os.scandir(r) as sd:
        for element in sd:
            if element.is_file():
                size_key = get_size_for_dict(element.stat().st_size)
                file_size_cnt[size_key][0] += 1
                file_size_cnt[size_key][1].add(os.path.splitext(element.name)[1][1:])

for k, v in file_size_cnt.items():
    file_size_cnt_dict[k] = tuple((v[0], list(v[1])))

with open(os.path.join(os.getcwd(), 'task_5_dict.json'), 'w+') as f:
    dump(file_size_cnt_dict, f)