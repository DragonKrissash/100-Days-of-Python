n=int(input("Enter a number: "))
bit=0
while n>0:
    n=n>>1
    bit+=1
print(f'The nearest 2 power is: {1<<bit-1}')