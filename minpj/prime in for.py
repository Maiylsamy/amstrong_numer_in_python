n =int(input('enter a number'))
ref = True
if n > 1:
    for x in range(2,n):
        if n%x == 0:
            ref = False
            break
else:
    ref = False
if ref:
    print('its prime number')
else:
    print('its not prime number')
