l=list(map(int,input().split()))
a=0
b=1
c=a+b
y=False
for i in l:
    if i==b:
        y=True
    else:
        y=False
        break
    a=b
    b=c
    c=a+b
if y:
    print('Yes')
else:
    print('No')