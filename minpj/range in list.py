m = [56,78,90,21,43,65,87]
for x in range(len(m)-2,-1,-2):
    a = m[x]
    if a%2 != 0:
        print(a) #65,21


l = [56,78,90,21,43,65,87]
cl = []
for x in range(len(l)-1,-1,-2):
    a = l[x]
    cl.append(l[x])
    if a%2 != 0:
        print(a)#87,43
print(cl)

n = [56,78,90,21,43,65,87]
for i in range(0,len(n)):
    if i%2 == 0:
        if n[i]%2 !=0:
            print(n[i])#43,87