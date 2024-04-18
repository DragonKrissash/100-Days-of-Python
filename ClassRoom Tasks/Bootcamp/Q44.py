word=input('Enter a string: ')
n=int(input('Enter the number of left shifts: '))
print(f'{word[n:]}{word[:n]}')