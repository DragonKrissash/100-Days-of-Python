def add(*args):
    res=0
    for num in args:
        res=res+num
    print(res)
add(1,2,3,4,5)

def calculate(**kwargs):
    print(kwargs)

calculate(add=3,mul=4)

class Car():
    def __init__(self,**kw):
        self.make=kw.get('make')
        self.model=kw.get('model')

car=Car(make='Tesla',model='S')
print(car.model)