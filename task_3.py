# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .

x = float(input('Введите координату X: '))
y = float(input('Введите координату Y: '))

if x > 0 and y >0 :
    print('Точка находится в первой четверти')
elif x < 0 and y > 0:
    print('Точка находится во второй четверти')
elif x < 0 and y < 0:
    print('Точка находится в третьей четверти')
elif x > 0 and y < 0:
    print('Точка находится в четвертой четверти')
else:
    print('Введите корректные координаты.')