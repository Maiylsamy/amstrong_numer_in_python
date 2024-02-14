n = eval(input('enter a number :'))
for i in n:
    x = ord(i)
    if 65<= x <=90:
        print(chr(x+32))
    elif 97<= x <=122:
        print(chr(x-32))