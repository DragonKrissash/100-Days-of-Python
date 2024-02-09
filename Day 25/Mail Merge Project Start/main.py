#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt','r') as file:
    names=file.read()
    names=names.split('\n')
    print(names)
with open('Input/Letters/starting_letter.txt','r') as file:
    letter=file.read()
    print(letter)
letters=[]
for name in names:
    letters.append(letter.replace('[name]',name))
for letter in letters:
    with open(f'Output/ReadyToSend/{names[letters.index(letter)]}.txt','w') as file:
        file.write(letter)

