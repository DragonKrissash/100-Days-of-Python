mat=[]
for i in range(2):
    row=list(map(int,input().split()))
    mat.append(row)
tra=[[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
print(tra)