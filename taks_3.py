from random import randint

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_random_phrase(*args: list):
    return ' '.join([arg[randint(0, len(arg) - 1)] for arg in args])


def new_get_random_phrase(*args, exlusion=[]):
    result = []
    for arg in args:
        phrase_list = arg.copy()
        for i in exlusion:
            if i in phrase_list:
                phrase_list.pop(phrase_list.index(i))

        if phrase_list != []:
            result.append(phrase_list[randint(0, len(phrase_list) - 1)])
        else:
            result.append(str(None))

    return ' '.join(result), result


def joke(n: int, repeated: bool = True):
    result = []
    exlusion = []
    for el in range(n):
        if repeated:
            result.append(get_random_phrase(nouns, adverbs, adjectives))
        else:
            phrase, i = new_get_random_phrase(nouns, adverbs, adjectives)
            exlusion.extend(i)
            result.append(phrase)
    return result


print(f'10 шуток (повторение): {joke(10)}')
print(f'10 шуток (без повторения): {joke(10, False)}')
