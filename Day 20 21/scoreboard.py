import turtle
from turtle import Turtle,Screen
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write(f'Score: {str(self.score)}', False, align='center', font=('Arial', 24, 'normal'))

    def updateScore(self):
        self.score+=1

        # self.penup()
        # self.hideturtle()
        # self.speed('fastest')
        # self.goto(0,280)
        # self.color('white')

    def updateScore(self):
        self.score+=1
        self.clear()
        self.write('Score: ' + str(self.score), False, align='center', font=('Arial', 24, 'normal'))

    def gameOver(self):
        self.goto(0,0)
        self.write('Game Over!',False,align='center',font=('Arial', 24, 'normal'))

