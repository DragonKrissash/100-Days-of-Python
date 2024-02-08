from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

padl=Paddle(-350, 0)
padr=Paddle(350, 0)
ball=Ball()
p1_score=Scoreboard(-200,150)
p2_score=Scoreboard(200,150)

game_is_on=True

screen.listen()
screen.onkey(padr.up,'Up')
screen.onkey(padr.down,'Down')
screen.onkey(padl.up,'w')
screen.onkey(padl.down,'s')
sleep_time=0.1
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()
    p1_score.showScore()
    p2_score.showScore()
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(padr)<50 and ball.xcor()>320:
        ball.bounce_x()
        p2_score.addScore()
        sleep_time*=0.9
    if ball.distance(padl)<50 and ball.xcor()<-320:
        ball.bounce_x()
        p1_score.addScore()
        sleep_time*=0.9
    if ball.xcor()>380:
        p1_score.gameOver(1)
        game_is_on=False
    if ball.xcor()<-380:
        p2_score.gameOver(2)
        game_is_on=False

screen.exitonclick()