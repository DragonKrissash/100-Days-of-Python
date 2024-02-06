import turtle
from turtle import Turtle,Screen
import random as rd
tim=Turtle()
tim.shape("turtle")
tim.color("red")
# for i in range(0,4):
#     tim.forward(100)
#     tim.left(90)
shapes=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
colors=['red','blue','green']
moves=[20,40,50,30,25,35,50,60,40]
dir=[0,90,180,270]
# tim.penup()
# tim.setx(-200)
# tim.sety(200)
# tim.pendown()
turtle.colormode(255)
for i in shapes:
    tim.pencolor(colors[shapes.index(i)%3])
    for j in range(i):
        tim.pensize(5)
        tim.forward(100)
        tim.right(360//i)
# for i in range(50):
#     tim.speed(10)
#     tim.pensize(15)
#     tim.pencolor((rd.randint(0,255),rd.randint(0,255),rd.randint(0 ,255)))
#     tim.setheading(rd.choice(dir))
#     tim.forward(30)

# def drawSpiro():
#     for i in range(40):
#         tim.pencolor(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
#         tim.speed(30)
#         tim.circle(100)
#         tim.left(10)
# for i in range(4):
#     drawSpiro()










screen=Screen()
screen.exitonclick()