for b in range(1,101):
    x=1
    p=0
    while x<=b:
        if b%x ==0:
            p += 1
        x += 1
    if p == 2 :
            print(b,' is prime number')
    else:
            print(b,' is not a prime number')