# genertate fabinnociss series or hemachandra series
n = eval(input("enter a number:"))
f = []
x= 0
y = 1
count = 0
while count < n:
    f = x + y
    print(f)
    x = y
    y = f
    count += 1
    # ========================
    # sum of the fabinnocies series