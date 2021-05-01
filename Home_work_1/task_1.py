# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Введите время в секундах: '))
time_to_minutes = duration % 60
time_to_hour = duration % 3600 // 60
time_to_day = duration % 86400 // 3600
time_to_week = duration % 604800 // 86400

if duration <= 60:
    print('до минуты:', ' <', time_to_minutes, '> ', 'сек')
elif duration <= 3600:
    print('до часа:', '<', time_to_hour, '>', 'мин', ' <', time_to_minutes, '> ', 'сек')
elif duration <= 86400:
    print('до суток:', '<', time_to_day, '>', 'час', '<', time_to_hour, '>', ' мин', ' <', time_to_minutes, '> ', 'сек')
else:
    print('<', time_to_week, '>', 'дн', '<', time_to_day, '>', 'час', '<', time_to_hour, '>', ' мин', ' <',
          time_to_minutes, '> ', 'сек')
