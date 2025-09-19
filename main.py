import time
from turtle import Screen, Turtle
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


my_snake = Snake()
screen.update()



# print(snake_position)
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.2)
#
#     for seg_no in range(len(segment) - 1, 0, -1):
#         new_x = segment[seg_no - 1].xcor()
#         new_y = segment[seg_no - 1].ycor()
#         segment[seg_no].goto(new_x, new_y)
#
#     segment[0].forward(20)

    # screen.onkey(move_snake_left,"o")
    # screen.onkey(move_snake_right,"p")




screen.exitonclick()