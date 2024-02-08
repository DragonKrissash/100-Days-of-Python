from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.color('white')
        self.score=0
    def gameOver(self,player):
        self.goto(-170,0)
        self.write(f'Player {str(player)} wins the game!',move=False,font=('Arial',24,'normal'))

    def addScore(self):
        self.score+=1

    def showScore(self):
        self.clear()
        self.write(self.score, move=False, font=('Arial', '30', 'normal'))