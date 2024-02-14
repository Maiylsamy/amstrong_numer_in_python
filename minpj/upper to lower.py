c = ['L', 'B', 'c', 'D']

for char in c:
    if char.islower():
        print(char.upper())
    elif char.isupper():
        print(char.lower())