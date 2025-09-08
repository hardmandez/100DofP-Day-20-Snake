import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


#Define new_snake_segment
snake_length = 3
snake_start_x = 0
snake_start_y = 0
snake=[]

for _ in range(snake_length):
    snake_start_x -= 20
    new_snake_segment=Turtle(shape="square")
    new_snake_segment.penup()
    new_snake_segment.color("white")
    # new_snake_segment.speed("fastest")
    new_snake_segment.goto(snake_start_x, snake_start_y)
    snake.append(new_snake_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in snake:
        segment.forward(20)





screen.exitonclick()