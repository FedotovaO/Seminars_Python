# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Введите номер четверти плоскости координат:'))
if num == 1:
    print('Возможные координаты: x < 0, y > 0')
if num == 2:
    print('Возможные координаты: x > 0, y > 0')
if num == 3:
    print('Возможные координаты: x < 0, y < 0')
if num == 4:
    print('Возможные координаты: x > 0, y < 0')