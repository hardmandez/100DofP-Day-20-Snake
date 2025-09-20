import time
from turtle import Screen, Turtle
from snake import Snake

#Define screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

my_snake = Snake()

#Game Loop
def game_loop():
    my_snake.movesnake()
    screen.update()
    my_snake.addsegment()
    screen.ontimer(game_loop, 200)


# print(snake_position)

game_loop()

screen.listen()
screen.onkey(my_snake.movesnakeleft,"Left")
screen.onkey(my_snake.movesnakeright,"Right")
screen.exitonclick()