n=int(input("Enter a number: "))
num=''
while n>0:
    if n%2==0:
        num=num+'0'
    else:
        num=num+'1'
    n=n//2
print(num[::-1])