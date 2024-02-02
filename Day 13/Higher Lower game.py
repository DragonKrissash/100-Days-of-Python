from art import logo,vs
from game_data import data
import random as rd
print (logo)
gameEnded=False
answered=False
score=0
while not gameEnded:
  if answered:
    ind=ind2
    ind2=rd.randint(0,len(data))
  else:
    ind=rd.randint(0,len(data))
    ind2=rd.randint(0,len(data))
  while ind==ind2:
    ind2=rd.randint(0,len(data))
  print(f'Person 1: Name: {data[ind]["name"]}, Description: {data[ind]["description"]}, Country: {data[ind]["country"]}')

  print('\n')
  
  print(f'Person 2: Name: {data[ind2]["name"]}, Description: {data[ind2]["description"]}, Country: {data[ind2]["country"]}')
  
  print('Who has more followers?')
  ans=int(input())

  if ans==1 and data[ind]['follower_count']>data[ind2]['follower_count']:
    print('Correct')
    answered=True
    score+=1
  elif ans==2 and data[ind]['follower_count']<data[ind2]['follower_count']:
    answered=True
    score+=1
  else:
    print('Wrong, you have lost the Game!')
    print(f'Your score is: {str(score)}')
    gameEnded=True
  

  