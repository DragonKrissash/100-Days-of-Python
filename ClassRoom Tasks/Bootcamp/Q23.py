#Swap 2 numbers
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
print(f'Before swapping, a:{a} b:{b}')
a=a^b
b=a^b
a=a^b
print(f'After swapping, a:{a} b:{b}')