#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

x = int(input('Введите номер дня недели: '))
if x > 0 and x <=5:
    print('Данный день не является выходным.')
elif x>0 and x>5 and x<=7:
    print('Данный день является выходным.')
else:
    print('Введите корректный номер дня недели.')