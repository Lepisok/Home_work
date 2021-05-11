get_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, element in reversed(list(enumerate(get_list))):
    element = element.replace('+' or '-', '')
    if element.isdigit():
        get_list.insert(i + 1, '"')
        get_list[i] = get_list[i].replace(element, f'{int(element):02}')
        get_list.insert(i, '"')
print(get_list)
print(id(get_list))

get_str = ' '.join(get_list)
get_str = get_str.split('"')
for element in range(1, len(get_str), 2):
    get_str[element] = get_str[element].replace(' ', '"')
get_str = ''.join(get_str)
print(get_str)
