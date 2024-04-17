# class Matrix:
#     def __init__(self,rows,cols):
#         self.rows=rows
#         self.cols=cols
#     def

rows1=int(input('Enter the number of rows of 1st matrix'))
cols1=int(input('Enter the number of cols of 1st matrix'))
print('Enter the elements of matrix 1: ')
mat1=[[]]
for r in range(rows1):
    m=[]
    for c in range(cols1):
        m.append(int(input()))
    mat1.append(m)
rows2=int(input('Enter the number of rows of 2nd matrix'))
cols2=int(input('Enter the number of rows of 2nd matrix'))
print('Enter the elements of matrix 2: ')
mat2=[[]]
for r in range(rows2):
    m=[]
    for c in range(cols2):
        m.append(int(input()))
    mat2.append(m)
if cols1==rows2:
    prod=[[]]

    for r in range(rows1):
        for c in range(cols2):
            p=0
            for a in range(cols1):
                p=p+mat1[r][a]*mat2[a][c]
            prod[r][c]=p
    for r in range(rows1):
        for c in range(cols2):
            print(prod[r][c],end=' ')
        print()



else:
    print('Matrices cannot be multiplied!')