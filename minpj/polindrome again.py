n = int(input("enter a number :"))
p = n
rev = 0
while 0 < n:
    r = n %10
    rev = rev * 10 +r
    n = n // 10
    print(rev)
if rev == p :
    print('its polindrom')
else:
    print('not polindrome')