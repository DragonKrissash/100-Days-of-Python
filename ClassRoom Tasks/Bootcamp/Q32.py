import math

n=int(input("Enter a number: "))
y=True
for i in range(2,int(math.sqrt(n))):
    if n%i == 0:
        y=False
        break
if y:
    print('Prime')
else:
    print('Not Prime')