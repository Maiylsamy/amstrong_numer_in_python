l = [1,4,25,79,2,46]
a = 0
for e in l :
    if e%2==0:
        a += e
        print(e)
print (a)

for e in l :
    if e%2!=0:
        print(e)
----------------sum
a=0
for s in l:
    a += s
print(a)
# or
digi = [ int(s) for s in l]
a = sum(digi)
print(a)
x=1
s=0
for p in l :
    while x<=p:
        if p%x==0
            s += 1
        x += 1
if s == 2:
    print('pr')
else:
    print('not prime')
myl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vowel = ['a','e','i','o','u']
for v in myl:
    if v in vowel:
        print(v)
    else:
        print('consonant')
c = ['L', 'B', 'c', 'D']

for char in c:
    if char.islower():
        print(char.upper())
    elif char.isupper():
        print(char.lower())
#         --------------------------
alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_list = ['a', 'c', 'd']

for char in input_list:
    if char in alphabet:
        position = alphabet.index(char) + 1
        print(f"{char} output is {position}")
