username=""
password=''
p1,p2,p3='','',''

def isValidLength(password:str):
    if len(password)>=10:
        return True
    else:
        return False

def istwoUpperCase(password:str):
    c=0;
    for let in password:
        if let.isupper():
            c+=1
    if c>=2:
        return True
    else:
        return False

def istwoLowerCase(password:str):
    c=0;
    for let in password:
        if let.islower():
            c+=1
    if c>=2:
        return True
    else:
        return False

def hasTwoDigits(password:str):
    c=0;
    for let in password:
        if let.isdigit():
            c+=1
    if c>=2:
        return True
    else:
        return False

def hasTwoSpecial(password):
    special_characters=('@','#','$','%','&','*','!')
    c=0
    for let in password:
        if let in special_characters:
            c+=1
    if c>=2:
        return True
    else:
        return False

def doesCharRep(password):
    c=0
    for i in range(1,len(password)):
        if password[i]==password[i-1]:
            c+=1
        if c>=4:
            return True
    return False


def checkUsername(password,username):
    for i in range(len(username)-2):
        sub=username[i:i+2]
        if sub in password:
            return True
    return False

def checkPassword(password,username,p1,p2,p3):
    if not isValidLength(password):
        print('The length of the password is not at least 10 characters! \nGive new password!')
    elif not istwoUpperCase(password):
        print("The password doesn't have atleast 2 upper case letters! \nGive new password!")
    elif not istwoLowerCase(password):
        print("The password doesn't have atleast 2 lower case letters! \nGive new password!")
    elif not hasTwoDigits(password):
        print("The password doesn't have atleast 2 digits in it! \nGive new password!")
    elif not hasTwoSpecial(password):
        print("The password doesn't have atleast 2 special characters! \nGive new password!")
    elif doesCharRep(password):
        print("The password has character repetition of 4 or more same characters! \nGive new password!")
    elif password==p1 or password==p2 or password==p3:
        print("The password must not be same as the last 3 passwords! \nGive new password!")
    elif checkUsername(password,username):
        print('The password has 3 or more consecutive characters from the username! \nGive new password!')
    else:
        print("It's a valid password!")
        return True
    return False
def giveInput():
    global password, username,p1,p2,p3
    print("Enter your username, password and last 3 passwords.")
    username=input()
    password=input()
    p1=input()
    p2=input()
    p3=input()

def getPassword():
    global password
    password=input()

is_valid_password=False
giveInput()
while(not is_valid_password):
    if checkPassword(password,username,p1,p2,p3):
        is_valid_password=True
    else:
        getPassword()