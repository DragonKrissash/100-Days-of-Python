EndOfBid=False
bidders={}
while(not EndOfBid):
  name=input("Enter your name!\n")
  price=int(input('Enter your bid amount: $'))
  bidders[name]=price
  print('Are there any other bidders? Enter y for yes and n for no!')
  reply=input()
  if reply=='n':
    EndOfBid=True
bidder=''
amt=0
for key in bidders.keys():
  if bidders[key]>amt:
    bidder=key
    amt=bidders[key]
print(f'The highest bid is made by {bidder} which is ${amt}!')