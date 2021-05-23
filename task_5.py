src_nums = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def get_unique_nums():
    nums_count = {}
    for item in src_nums:
        if nums_count.get(item):
            nums_count[item] += 1
            continue
        nums_count[item] = 1
    return [key for key, value in nums_count.items() if value == 1]


print(get_unique_nums())
