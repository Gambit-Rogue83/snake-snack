from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-Snack")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

crashed = False

while not crashed:
    screen.update()
    time.sleep(0.1)

    snake.move()


    #Detect food contact
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -298 or snake.head.ycor() > 300 or snake.head.ycor() < -285:
        crashed = True
        score.game_over()

    #Detect tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            crashed = True
            score.game_over()













screen.exitonclick()