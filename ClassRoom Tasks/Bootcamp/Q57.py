l=list(map(int,input('Enter the array elements: ').split()))
n=int(input('Enter the circular index: '))
print(f'{l[n:]}{l[:n]}')