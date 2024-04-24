import math


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def __add__(self, other):
        return Complex(self.real+other.real,self.img+other.img)


    def __str__(self):
        return f'{self.real}+{self.img}i'

    def __int__(self):
        return int(math.sqrt(self.real**2+self.img**2))

    def __lt__(self, other):
        if self.real<=other.real:
            return True
        else:
            return False

    def __custom__(self):
        print('This is custom')

a=Complex(5,4)
b=Complex(1,2)
c=a+b
l=[a,b,c]
for i in l:
    for j in l:
        if i<j:
            t=i
            i=j
            j=t
print(l[0],l[1],l[2])