l1=list(map(int,input('Enter the first array elements: ').split()))
l2=list(map(int,input('Enter the second array elements: ').split()))
inter=[]
for l in l2:
    if l in l1:
        inter.append(l)
print(inter)