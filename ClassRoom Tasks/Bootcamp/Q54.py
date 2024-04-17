s1=input("Enter word 1: ")
s2=input("Enter word 2: ")
y=False
for i in s1:
    if i in s2:
        y=True
    else:
        y=False
        break
if y:
    print("Yes")
else:
    print("No")