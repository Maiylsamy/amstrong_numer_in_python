def fibonacci(n): #using function sum of the fibonacci series
    seq_feb = [0,1]
    while len(seq_feb) <= n:
        seq_feb.append(seq_feb[-1]+seq_feb[-2])
    sumfeb = sum(seq_feb)
    return sumfeb
n = eval(input('enter a number :'))
result = fibonacci(n)
print(result)


