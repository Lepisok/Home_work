def tutors_and_klasses_gen(_tutors, _klasses):
    for idx in range(len(_tutors)):
        if idx >= len(_klasses):
            yield _tutors[idx], None
        else:
            yield _tutors[idx], _klasses[idx]


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tutors_and_klasses = tutors_and_klasses_gen(tutors, klasses)
print(type(tutors_and_klasses))
print(*tutors_and_klasses)
# StopIteration
print(next(tutors_and_klasses))
