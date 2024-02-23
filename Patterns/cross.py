n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if i==j:
            print("\\",end="")
        elif j==n-1-i:
            print('/',end='')
        else:
            print('*',end="")
    print()
