n=int(input("Enter a number: "))
def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
print(f(n))