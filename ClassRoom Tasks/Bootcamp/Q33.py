import math

a=int(input("Enter the first term: "))
r=int(input("Enter the ratio: "))
n=int(input("Enter the number of terms: "))
for i in range(0,n):
    print(a*math.pow(r,i),end=' ')