from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time
screen=Screen()
food=Food()
scoreboard=ScoreBoard()
screen.setup(1280,720)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer (0)
screen.listen()

snake=Snake()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.moveFood()
        snake.extend()
        scoreboard.updateScore()
    if snake.head.xcor()>630 or snake.head.ycor()>340 or snake.head.xcor()<-630 or snake.head.ycor()<-340:
        scoreboard.gameOver()
        game_is_on=False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.gameOver()
            game_is_on=False



 





screen.exitonclick()