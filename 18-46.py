# Космонавты кодируют сигнал с помощью последовательностей из нулей и единиц длины - 22 (длина - это общее количество нулей и
# единиц),
# в которых никакие три единицы не должны стоять рядом. Определите количество таких последовательностей.
# Ответ запишите числом, без дополнительных пробелов и символов до и после ответа (например: 1001).
from itertools import *

k = 0
s=[-11,-2,-4,-10,-9,4,-5,-18,-16,5,-6,-19,0,-7,11,-17,11,9,-7,-11,19,-16,-11,-4,19,-6,-6,-15,1,11,-1,-16,12,0,-15,-13,11,-19,-15,-18,-20,7,-8,17,-4,16,6,-5,-3,-8,17,-2,2,1,-2,19,-6,13,-7,-8,9,-13,4,-19,-4,20,20,-10,9,13,18,15,-15,-16,20,15,19,-13,6,17,-9,-6,-3,-1,19,5,2,-14,-20,15,20,-7,-13,16,-16,16,-4,1,-20,-11]
#s = [10, -5, 4, 9, -1, 5, -8, -1]
ss = set()
for i in range(0, len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i] + s[j] == 7:
            if s[i] > s[j]:
                #print(s[i], s[j])
                ss.add(str(s[i]) + str(s[j]))
            else:
                #print(s[j], s[i])
                ss.add(str(s[j]) + str(s[i]))
#print(k)
print(len(ss))
# print('3:',list(combinations(s,2)))
