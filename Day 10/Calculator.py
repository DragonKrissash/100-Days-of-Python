def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b

options={"+":add,
         "-":sub,
         "*":mul,
         "/":div
        }
n1=int(input("Enter the first number!\n"))
n2=int(input("Enter the second number!\n"))
for sym in options.keys():
  print(sym)
print("Choose an option from above\n")
opr=input()
if opr=="+":
  res=add(n1,n2)
elif opr=="-":
  res=sub(n1,n2)
elif opr=="*":
  res=mul(n1,n2)
else:
  res=div(n1,n2)

print(f'The result is = {res}')