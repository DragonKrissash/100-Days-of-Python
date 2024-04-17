print('Enter the number of rows: ')
r=int(input())
m=[]
for i in range(r):
    n=list(map(int,input(f'Enter the elements of {i}th row').split()))
    m.append(n)
for i in m:
    print(sum(i))