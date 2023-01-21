# Демо 2022
file = open('27_B.txt', 'r')
mas = file.readlines()
mas = list(map(int, mas))
print("mas: ", mas)
s = []
sumindex = 0
for i in range(len(mas)):
    sumindex += mas[i]
    s.append(sumindex)
print("s: ", s)
mas43 = []
for i in range(43):
    mas43.append({})

for i in range(len(mas)):
    mas43[s[i] % 43].update({s[i]: i})
print(mas43)

maxmas = []
masnum = []
maxi = 0
for i in range(len(mas43)):
    n = len(list(mas43[i].items()))
    if n > 1:
        serchmax = list(mas43[i].items())[n - 1][0] - list(mas43[i].items())[0][
            0]  # разность между первым последним элементом и первым (суммы)
        serchcol = list(mas43[i].items())[n - 1][1] - list(mas43[i].items())[0][1]  # для порядковых номеров
        maxmas.append(serchmax)
        masnum.append(serchcol)

maxi = 0
for i in range(len(maxmas)):
    print(maxmas[i])
    if maxmas[i] > maxi:
        maxi = maxmas[i]
        j = i
print(maxi, masnum[j])
