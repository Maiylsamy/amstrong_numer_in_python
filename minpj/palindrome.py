x = int( input('entr  NO:'))
p = x
rev = 0
while 0<x :
    r = x%10
    rev = rev*10+r
    x = x//10
    print(rev)
if p == rev:
    print(p,'is polyndrome')
elif p != rev:
    print(p,'is not polyndrome')
# print a single value separatly
y = int( input('entr  NO:'))
rev = 0
while 0<y :
    re = y %10
    p = rev*10+re
    y = y//10
    print(p)