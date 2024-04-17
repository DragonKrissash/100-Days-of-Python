import math
def isprime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
n=int(input('Enter the number of prime numbers: '))
primes=[]
for i in range(2,1000):
    if isprime(i):
        primes.append(i)
        n=n-1
    if n==0:
        break
print(primes)