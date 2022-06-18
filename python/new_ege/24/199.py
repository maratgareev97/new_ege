'''199)	Текстовый файл 24-197.txt содержит строку из заглавных латинских букв
X, Y и Z, всего не более чем из 106 символов. Определите максимальное количество
идущих подряд троек символов X*X или Y*Y, где * обозначает один любой символ.'''

file=open('24-197.txt', 'r')
c=file.readline()
max=0
for m in range (3):
    k=0
    for i in range (m, len(c)-2, 3):
        if (c[i]=='X' and c[i+2]=='X') or (c[i]=='Y' and c[i+2]=='Y'):
            k+=1
        else:
            if k>max:
                max=k
            k=0
    if k>max:
        max=k
print(max)

