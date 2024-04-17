l=list(map(int,input().split()))
summ=0
for i in l[::2]:
    summ=summ+i
print(summ)