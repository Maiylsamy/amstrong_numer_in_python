x = int(input('enter a number :'))
i = 0
j = 1
count = 0
fab_list = []
while  count < x:
    fab_list.append(i)
    t =i+j
    print(i)
    i = j
    j = t
    count +=1
n = sum(fab_list)
print(fab_list)
print(n)