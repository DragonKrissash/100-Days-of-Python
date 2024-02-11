#Password Generator Project
from random import randint,shuffle,choice
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_list = [choice(letters) for i in range(randint(8, 10))]
sym_list=[choice(symbols) for i in range(randint(2, 4))]
num_list=[choice(numbers) for i in range(randint(2, 4))]

password_list=letter_list+sym_list+num_list
shuffle(password_list)
def genPassword():
  password = [let for let in password_list]
  password="".join(password)
  return password
