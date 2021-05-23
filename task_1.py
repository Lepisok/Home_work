def odd_nums(n):
    for num in range(1, n + 1):
        if num % 2:
            yield num


odd_to_15 = odd_nums(15)
print(*odd_to_15)