x = int (input('enter a num :'))
rev = 0
while x > 0:
    r = x%10
    rev = rev*10+r
    x = x // 10
    print(rev)
sum_poli = [int(z)for z in str(rev)]
print(sum(sum_poli))



