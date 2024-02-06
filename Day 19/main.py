from turtle import Turtle,Screen
import random as rd
screen=Screen()
screen.setup(width=500,height=400)
is_game_on=False
user_bet=screen.textinput(title='Make your bet',prompt='Which turtle will win the race? Enter a color: ')
color=['red','green','blue','orange','yellow','purple']
y=-100
turtles=[]
for i in range(6):
    tim=Turtle(shape='turtle')
    tim.color(color[i])
    tim.penup()
    tim.goto(x=-230,y=y)
    y+=30
    turtles.append(tim)

if user_bet:
    is_game_on=True

while is_game_on:
    for tim in turtles:
        if tim.xcor()>230:
            win_color=tim.pencolor()
            if win_color==user_bet:
                print('You have won')
                is_game_on=False
            else:
                print('You have lost')
                is_game_on=False
    for tim in turtles:
        tim.forward(rd.randint(1,10))

screen.exitonclick()