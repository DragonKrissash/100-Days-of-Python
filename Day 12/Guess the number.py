logo='''
   ____                       _   _                                  _               _ 
  / ___|_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __| |
 | |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| |
 | |_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |  |_|
  \____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  (_)
                                                                                       
'''
import random as rd
numToPredict=rd.randint(1,101)
print(logo)
print('Choose the game difficulty - Easy or Hard')
difficulty = input().lower()
if difficulty=='easy':
    moves=10
else:
    moves=5
print('Enter a number')
while moves>0:
    userInput=int(input())
    if userInput>numToPredict:
        print('Too High')
        moves=moves-1
    elif userInput<numToPredict:
        print('Too Low')
        moves-=1
    else:
        print('You Win!')
        break
if moves==0:
    print('You Lose')
    print('The Number was ', numToPredict)