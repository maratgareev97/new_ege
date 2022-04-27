a = [3, 13, 43, 17, 16, 10, 50, 36, 12, 5]
f=open("27-97b.txt")
a=f.readlines()
for i in range(len(a)):
   a[i]=int(a[i])
#a=[11,15,8,14,22,24,10]
#print("a:", a)
# заполняем массив накопленных сумм
s = []
s1=0
b = 0
k = 988  # кратность
for i in range(len(a)):
    b += a[i]
    s.append(b)
#print("s", s)

for i in range(len(a)):
    if a[i]%k==1:
        s1+=1

sp = []
for i in range(k):
    sp.append(0)
#print(sp)
count = 0

for i in range(len(a)):
    sp[s[i] % k] += 1
#print(sp)


s = 0
for i in range(k):
    s += (sp[i] * (sp[i] - 1)) // 2

print(s+sp[0]) # прибавляем т.к. в нулевой ячейке лежат нулевые чисто кратные k
