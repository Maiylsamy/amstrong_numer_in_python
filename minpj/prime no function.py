def is_prime(num):
    if num<2 :
        return False
    for i in range(2,int(num*0.5)+1):
        if num%i==0:
            return False
    return True


def nth_prime(n):
    count = 0  # Counter for prime numbers found
    num = 1  # Starting number to check for primality

    while count < n:
        num += 1  # Move to the next number
        if is_prime(num):
            count += 1  # If the current number is prime, increment the counter

    return num  # Return the nth prime number
n = int(input("Enter the value of n: "))
result = nth_prime(n)
print(f"The {n}th prime number is: {result}")
