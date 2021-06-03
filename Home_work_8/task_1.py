import re

valid_email = ['123abc@mail1.com', '123_abc@mail.2com', '123-abc@mail3.3com',
               '1.2.3.a.b.c@4mail4.4com4', '1-2-3-a-b-c@ma5il.com', '1_2-3.abc@6m6a6i6l6.6c6o6m6',
               '             1_2-3.abc@mail.com']
not_valid_email = ['123abc@mailcom', '123abc.@mail.com', '.123abc@mail.com',
                   '123a..bc@mail.com', '123abc-@mail.com', '-123abc@mail.com',
                   '123--abc@mail.com', '123 abc@mail.com', '123abc @mail.com']

RE_TASK_1 = re.compile(r'(?P<username>^\w+([._-]\w+)*)@(?P<domain>\w+\.\w+)')

RE_TASK_2 = re.compile(r'^([0-9a-f.:]+) - - \[(.*)\] \"(\w+) (.*?)\" (\d+) (\d+) ', flags=re.IGNORECASE)


def email_parse(email):

    if s := RE_TASK_1.search(email.strip()):
        return s.groupdict()
    raise ValueError(f'{email} - not valid email')


def log_line_parse(log_str):
    if s := RE_TASK_2.search(log_str):
        return s.groups()
    raise ValueError(f'--- NOT VALID --- {log_str}')  


def task_1():
    for elem in valid_email + not_valid_email:
        try:
            print(elem, email_parse(elem))
        except ValueError as e:
            print(e)


def task_2():
    with open('nginx_logs.txt', encoding='utf8') as f:
        for line in f:
            try:
                print(log_line_parse(line))
            except ValueError as e:
                print(e)


if __name__ == '__main__':
    task_1()
    task_2()
