for i in range(1,15):
    for j in range(1,15):
        if i + j <= 14:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()


for l in range(1,8):
    for k in range(1,8+l-1):
        if l+k <= 7:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()


for a in range(1,5):
    for b in range(1,1+a):
        print('*',end=' ')
    print()


for c in range(4,0,-1):
    for d in range(1,1+c):
        print('*',end=' ')
    print()

for g in range(6,0,-1):
    for h in range(1,7):
        if g + h <= 6 :
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()
