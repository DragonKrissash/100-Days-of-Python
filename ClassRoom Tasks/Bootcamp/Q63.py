def sumdig(n):
    if n==0:
        return 0
    else:
        return int(n%10)+sumdig(n/10)
print(sumdig(123))