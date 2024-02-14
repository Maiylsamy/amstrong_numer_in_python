x = int(input('enter a number'))
ams = 0
for c in str(x):
    cube = int(c)
    ams  += cube**3
    print(ams)
if ams == x :
    print('it is amstrong no.',x)
else:
    print('it is not amstrong.',x)

