l1=list(map(int,input('Enter the first array elements: ').split()))
l2=list(map(int,input('Enter the second array elements: ').split()))
for l in l2:
    l1.append(l)
print(l1)