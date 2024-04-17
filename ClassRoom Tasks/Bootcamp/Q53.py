l=list(map(int,input().split()))
num=0
for i in range(len(l)):
    num=num^l[i]
print(num)