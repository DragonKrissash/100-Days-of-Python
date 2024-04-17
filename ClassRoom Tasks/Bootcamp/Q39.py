import math

rad=int(input("Enter the value of radius: "))
for i in range(-rad,rad+1):
    for j in range(-rad,rad+1):
        if math.sqrt(i**2+j**2)<=rad:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()