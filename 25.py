'''Пусть M(k) = 7 000 000 + k, где k – натуральное число.
Найдите пять наименьших значений k, при которых M(k) нельзя представить
в виде произведения трёх различных натуральных чисел, не равных 1.
В ответе запишите найденные значения k в порядке возрастания.'''
def F(n):
    s=n
    i=2
    m=set()
    while n>1:
        if n%i==0:
            n=n//i
            m.add(i)
            #print(m)
        else:
            i+=1
    if {s}<=m:
        return True

#print(F(37))

a=7000000
for z in range(1,1000):
    s=z+a
    k=0
    mas=[]
    for n in range(2,s):
        if s%n==0 and F(n)==True:
            k+=1
            mas.append(n)
            if k>2:
                break
    if (k==2 and mas[0]*mas[1]==s) or F(s)==True:
        print(mas,s)





