# import colorgram
# colors=colorgram.extract('20_001.jpg',30)
# rgb_colors=[]
# for color in colors:
#     rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
import turtle
import random as rd
colors=[(199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228), (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35), (76, 40, 48), (9, 68, 47), (90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149), (179, 201, 186), (173, 153, 159), (212, 183, 176), (151, 114, 119), (177, 198, 203), (206, 184, 190), (37, 73, 84), (45, 74, 63), (48, 66, 80)]
from turtle import Turtle,Screen
turtle.colormode(255)
tim=Turtle()
tim.shape('turtle')
# tim.begin_fill()
# tim.circle(100)
# tim.end_fill()
tim.penup()
tim.setx(-300)
tim.sety(-300)
def draw_row():
    for i in range(10):
        tim.pendown()
        tim.dot(20,rd.choice(colors))
        tim.penup()
        tim.forward(50)
tim.speed('fastest')
for i in range(10):
    draw_row()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)





screen=Screen()
screen.exitonclick()
