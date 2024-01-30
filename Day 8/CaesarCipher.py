alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
  gen_text=''
  shift_ind=0
  for i in text:
    if i in alphabet:
      if direction =='encode':
        shift_ind=alphabet.index(i)+shift
        if shift_ind>=len(alphabet):
          shift_ind=shift_ind-26
      else:
        shift_ind=alphabet.index(i)-shift
        if shift_ind<0:
          shift_ind=26+shift_ind
      gen_text=gen_text+alphabet[shift_ind]
    else:
      gen_text=gen_text+i
  print(gen_text)
      

end=False
while not end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction=='encode' or direction=='decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if(shift>26):
      shift=shift%26;
    caesar(direction,text,shift)
  else:
    print('Wrong Input!')
  shouldEnd=input("Type YES to try again or NO to stop!\n")
  if shouldEnd=="NO":
    end=True