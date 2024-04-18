l1=list(map(int,input('Enter the first array elements: ').split()))
l2=list(map(int,input('Enter the second array elements: ').split()))
subtract=[]
for l in range(len(l1)):
    subtract.append(abs(l1[l]-l2[l]))
print(subtract)