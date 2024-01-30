stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
display=['_' for i in range(0,len(chosen_word))]
chosen_word=list(chosen_word)
end=False
lifes=len(stages)
letter_checked=False
while not end:
  guess = input("Guess a letter: ").lower()
  if guess in chosen_word:
    for letter in chosen_word:
      if(guess==letter):
        if(display[chosen_word.index(guess)]=='_'):
          display[chosen_word.index(guess)]=guess
          chosen_word[chosen_word.index(guess)]='_'

  else:       
    lifes=lifes-1
    print("Try again!")
    print(stages[lifes])
  print(display)
  if '_' not in display:
    print("You win")
    end=True
  if lifes==0:
    print("You lose")
    end=True

