def thesaurus(*args):
    result = dict()
    for arg in args:
        if arg[0] in result:
            result[arg[0]].append(arg)
    else:
        result[arg[0]] = [arg]
    return result


print(f'thesaurus("Иван", "Мария", "Петр", "Илья"): {thesaurus("Иван", "Мария", "Петр", "Илья")}')
