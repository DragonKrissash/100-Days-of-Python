from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        # self.hideturtle()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.setposition(x=xcor,y=ycor)
        self.setheading(90)
        # self.showturtle()
    def up(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)

    def down(self):
        y=self.ycor()-20
        self.goto(self.xcor(),y)
