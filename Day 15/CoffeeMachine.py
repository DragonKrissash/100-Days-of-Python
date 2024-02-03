MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

res={
    'water':300,
    'milk':200,
    'coffee':100,
    'money':0
}
curr_value={
    'quar':0.25,
    'dime':0.1,
    'nick':0.05,
    'penn':0.01
}

def showReport():
    print(f'Water: {res["water"]}\n'
          f'Milk: {res["milk"]}\n'
          f'Coffee: {res["coffee"]}\n'
          f'Money: {res["money"]}')

def askMoney():
    penn=int(input('How many pennies?'))
    nick=int(input('How many nickels?'))
    dime=int(input('How many dimes?'))
    quar=int(input('How many quarters?'))
    tot_amt=penn*0.01+nick*0.05+dime*0.1+quar*0.25
    return tot_amt


def makeCoffee(prompt,tot_amt):
    res['water'] = res['water']-MENU[prompt]['ingredients']['water']
    res['water'] = res['coffee'] - MENU[prompt]['ingredients']['coffee']
    res['water'] = res['milk'] - MENU[prompt]['ingredients']['milk']
    balance=tot_amt-MENU[prompt]['cost']
    res['money']=res['money']+MENU[prompt]['cost']
    print(f'Here is your {prompt} and the balance amount: {balance}\n'
          f'Please come again!\n')

def choice(prompt):
    available=False
    prompt_ing=MENU[prompt]['ingredients']
    if res['water']>=prompt_ing['water'] and res['milk']>=prompt_ing['milk'] and res['coffee']>=prompt_ing['coffee']:
        available=True
    else:
        available=False
    if available:
        tot_amt=askMoney()
        if tot_amt>=MENU[prompt]['cost']:
            makeCoffee(prompt,tot_amt)
        else:
            print('Payment is not sufficient! Money has been returned!')
    else:
        print('Sorry we are out of resources!')

turn_on=True
while turn_on:
    prompt=input('What would you like to have?: ')
    if prompt=='report':
        showReport()
    elif prompt in MENU.keys():
        choice(prompt)
    else:
        turn_on=False

