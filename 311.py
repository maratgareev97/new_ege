'''75)	В некоторой системе счисления записи десятичных чисел 68 и 94 заканчиваются на 3.
Определите основание системы счисления.'''
for i in range (1, 100):
    if 68%i==3 and 94%i==3:
        print(i)
