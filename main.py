from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-Snack")
screen.tracer(0)

starting = [(0, 0), (-20, 0), (-40, 0)]

snake = []

for position in starting:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    snake.append(new_segment)

crashed = False

while not crashed:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake) -1, 0, -1):
        new_x = snake[seg_num -1].xcor()
        new_y = snake[seg_num -1].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].fd(20)
    snake[0].left(90)













screen.exitonclick()