l=[[0 for j in range(4)] for i in range(4)]
row=4; col=4; i=0; j=0; jump=0;ind=1
while row>0 and col>0:
    jump=0
    while jump<col:
        l[i][j]=ind;jump+=1;j+=1;ind+=1
    jump=0;row=row-1;i+=1;j=j-1
    while jump<row:
        l[i][j]=ind;ind+=1;jump+=1;i+=1
    i=i-1;col-=1;jump=0;j=j-1
    while jump<col:
        l[i][j]=ind;ind+=1;j-=1;jump+=1
    j=j+1;row-=1;i-=1;jump=0
    while jump<row:
        l[i][j]=ind;ind+=1;i-=1;jump+=1
    jump=0;j+=1;col-=1;i-=3
for i in range(4):
    print(l[i])