############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. https://replit.com/@appbrewery/blackjack-final?v=1
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random as rd
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
userCards = rd.sample(cards,2)
userScore=sum(userCards)
compCards = rd.sample(cards,1)
compScore=sum(compCards)
print(f'Your cards are {userCards}')
print(f'Your score is {str(userScore)} and computer score is {str(compScore)} \nDo you wanna draw another card? Y for yes and N for no.')
userInp=str.lower(input())
if userInp=='y':
    userCards.append(rd.choice(cards))
    userScore=sum(userCards)
    print(f'Your score is {str(userScore)}')
    if userScore>21:
        print('You lose')
    else:
        compCards=compCards.append(rd.choice(cards))
        compScore=sum(compCards)
        print(f'Computer Score is {str(compScore)}')
        if compScore>21:
            print('You win')
        else:
            if userScore>compScore:
                print('You win')
            else:
                print('You lose')
else:
    compCards.append(rd.choice(cards))
    compScore=sum(compCards)
    UserScore=sum(userCards)
    print(f'Computer cards are {compCards} and score is {str(compScore)}')
    print(f'Your cards are {userCards} and score is {str(UserScore)}')
    if compScore>21:
        print('You win')
    else:
        if UserScore<compScore:
            print('You win')
        else:
            print('You lose')
