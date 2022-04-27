f = open("27-88a.txt") # 17
a1 = f.readlines()
a1 = [-7, 32, -3, -17, 9, -8, 3, 2, -2, 2, -17, -1, 2]
summ=[]
ss=0
for i in range(len(a1)):
    a1[i] = int(a1[i])
    ss+=a1[i]
    summ.append(ss)

#print(max(a1), min(a1))
print("a1  ",a1)
print("summ",summ)
print(max(summ),min(summ))


def prost(n):
    k = 0
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if abs(n) % i == 0:
            k += 1
            break
    if k == 0 and abs(n) != 1 and n < 0:
        return True
    else:
        return False


a = []
for i in range(len(a1)):
    if prost(a1[i]) == False:
        a.append(0)
    else:
        a.append(a1[i])
#print(a1)
print(a)

k = 0
b = []
if a[0] < 0:
    i = 1
else:
    i = 0
while i < len(a):
    if a[i] >= 0:
        k += 1
    else:
        b.append(k)
        k = 0
    i = i + 1
b.append(k)
maxim = 0
for i in range(len(b) - 1):
    if b[i] + b[i + 1] > maxim:
        maxim = b[i] + b[i + 1]
#print(b)
print(maxim)
k = 0
maximka = 0
for i in range(len(a)):
    if a[i] == 0:
        k += 1
    else:
        if k > maximka:
            maximka = k
            index = i
        k = 0
print(maximka, index)
