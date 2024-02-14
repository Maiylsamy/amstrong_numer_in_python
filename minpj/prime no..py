boin =0 #som of the prime
primecount=0 #count of prime numbers
for x in range(1,7):
    a=1
    count = 0
    while a<=x:
        if x%a==0:
            count += 1
        a += 1

    if count == 2:
        print(x)
        boin+=x
        primecount += 1

print(primecount) #count of prime
print(boin) #(2,3,5) 0/p 10

