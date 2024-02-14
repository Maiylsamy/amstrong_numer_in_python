# lowercase 97 = a to 122 = z
# uppercase 65 = A to 90 = Z
print(chr(65))
# or
x = 90
y = chr(x)
print(y)
# -------------
# same as lowercase see above
# ---------------
# now we print case to int (use ord on print)
print(ord('a')) #lower
print(ord('z'))
print(ord('A'))#upper
print(ord('Z'))
# wpp based on this
a =  97
z = ["a",'e','i','o','u']
while a <= 122:
    ch = chr(a)
    if ch in z :
        print (ch)
    a +=1