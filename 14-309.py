'''Значение арифметического выражения 103∙7**103 – 5∙7**57 + 98 записали в системе счисления с
основанием 7. Найдите сумму цифр получившегося числа и запишите её в ответе в десятичной
системе счисления.'''
x=103*7**103-5*7**57+98
d=0
while x >0:
    d+=x%7
    x=x//7
print(d)