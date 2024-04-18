# l=list(map(int,input('Enter the array elements: ').split()))
# n=int(input('Enter the circular index: '))
# print(f'{l[n:]}{l[:n]}')
# import math
#
# n=int(input('Enter a number: '))
# x=int(math.log(n-n%2,2))
# print(x)

a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a
for i in b:
    if i not in a:
        c.append(i)
print(c)
