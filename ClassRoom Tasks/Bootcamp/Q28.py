sleeper=200
ac3=1000
ac2=2000
ac1=3000
month_pass=int(input("Enter your type of pass. \n1 - One time \n2 - Monthly pass \n"))
ticket=int(input('Enter your type of ticket. \n 1 - 1AC \n 2 - 2AC \n 3 - 3AC \n 4 - Sleeper \n'))
if month_pass==1:
    if ticket==1:
        print(f'Your ticket cost is: {ac1}')
    elif ticket==2:
        print(f'Your ticket cost is: {ac2}')
    elif ticket==3:
        print(f'Your ticket cost is: {ac3}')
    else:
        print(f'Your ticket cost is: {sleeper}')
else:
    if ticket==1:
        print(f'Your monthly pass cost is: {ac1*30*(8/10)}')
    elif ticket==2:
        print(f'Your monthly pass cost is: {ac2*30*(8/10)}')
    elif ticket==3:
        print(f'Your monthly pass cost is: {ac3*30*(8/10)}')
    else:
        print(f'Your monthly pass cost is: {sleeper*30*(8/10)}')