try:
    file=open('a.txt','w')
except FileNotFoundError as e:
    print(e)
else:
    pass
finally:
    file.close()

height=45
weight=65
bmi=weight/height**2
if height>3:
    raise ValueError('Height is not real!')