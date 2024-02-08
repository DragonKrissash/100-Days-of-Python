from turtle import Turtle
import random as rd
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.up()
        self.speedNum=7
        self.speed(self.speedNum)
        dir = [1, -1]
        self.y_move=10*rd.choice(dir)
        self.x_move=10*rd.choice(dir)


    def move(self):
        x=self.xcor()+self.x_move
        y=self.ycor()+self.y_move
        self.goto(x,y)

    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self):
        self.x_move*=-1


