def number_translate_adv(number):
    if number.istitle():
        print(number_translate.get(number.lower()).capitalize())
    else:
        print(number_translate.get(number))


number_translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

number_translate_adv('One')
number_translate_adv('two')
number_translate_adv('five')
number_translate_adv('Nine')
number_translate_adv('nine')
number_translate_adv('twenty')