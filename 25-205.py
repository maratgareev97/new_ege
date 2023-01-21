s = open('26.txt', 'r')

st = s.readlines()
n = len(st)
s.close()
print(n)

# for x in range(1236147000,1322548000+1):
for x in range(1236147000,1322548000+1,10):
    s = open('26.txt', 'r')
    for i in range(n):
        st = s.readline()
        st = st.split()
        #print(st)
        if len(st)<2:
            print(st,n)
        if len(st)==2:
            if int(st[0]) <= x <= int(st[1]):
                pass
    s.close()
# n=int(st[0])
# minim=int(st[1])
# print(n)
