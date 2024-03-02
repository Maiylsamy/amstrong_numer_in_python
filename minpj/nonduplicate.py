my_list =[10,5,2,5,8,10,4,6,5,10]
uni_lis = []
for i in my_list:
    if i not in uni_lis:
        uni_lis.append(i)
print(uni_lis)
# another simple way u convert into set
a = set(my_list)
print(a)
