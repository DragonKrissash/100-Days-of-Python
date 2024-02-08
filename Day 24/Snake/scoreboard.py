from turtle import Turtle,Screen
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open('data.txt') as file:
            self.highscore=int(file.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write(f'Score: {str(self.score)} High Score: {str(self.highscore)}', False, align='center', font=('Arial', 24, 'normal'))
    def updateScore(self):
        self.score+=1
    def updateScore(self):
        self.score+=1
        self.clear()
        self.write(f'Score: {str(self.score)} High Score: {str(self.highscore)}', False, align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open('data.txt','w') as file:
                file.write(str(self.highscore))
        self.score=0
        self.updateScore()

    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write('Game Over!',False,align='center',font=('Arial', 24, 'normal'))

