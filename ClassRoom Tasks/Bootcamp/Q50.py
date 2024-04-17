print('Enter the number of rows: ')
r=int(input())
m=[]
for i in range(r):
    n=list(map(int,input(f'Enter the elements of {i}th row').split()))
    m.append(n)
sum=0
for i in range(len(m[0])):
    for j in range(len(m)):
        sum=sum+m[j][i]
    print(sum)