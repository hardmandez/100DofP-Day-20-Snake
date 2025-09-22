import time
import math
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score

my_snake = Snake()
food = Food()
score = Score()

#Define screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Grub")
# turtle.goto(0, 295)
# turtle.write(str("Score"), align="center", font=("Arial", 10, "bold"))
screen.tracer(0)



#Game Loop
def game_loop():
    my_snake.movesnake()
    snake_position = round(my_snake.segment[0].xcor()), round(my_snake.segment[0].ycor())
    # print(snake_position[0])
    food.createfood()
    food_position = food.food_position
    # print(food_position[0])
    screen.update()
    print(len(my_snake.segment))
    # my_snake.addsegment()

    #Check for food collision.
    if abs(snake_position[0] - food_position[0]) <= 15 and abs(snake_position[1] - food_position[1]) <= 15:
        my_snake.addsegment()
        food.food_counter = 0
        score.score += 1
        score.displayscore()
    screen.ontimer(game_loop, 200)

    # Check for snake collision.
    my_snake.checkcollision()

    #Check for out of screen.
    my_snake.checkinbound()



# print(snake_position)

game_loop()

screen.listen()
screen.onkey(my_snake.movesnakeleft,"Left")
screen.onkey(my_snake.movesnakeright,"Right")
screen.exitonclick()