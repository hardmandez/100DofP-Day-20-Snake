import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


#Define new_snake_segment


# def move_snake_left():
#     segment[0].left(90)
#
# def move_snake_right():
#     segment[0].right(90)



print(snake_position)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    for seg_no in range(len(segment) - 1, 0, -1):
        new_x = segment[seg_no - 1].xcor()
        new_y = segment[seg_no - 1].ycor()
        segment[seg_no].goto(new_x, new_y)

    segment[0].forward(20)

    # screen.onkey(move_snake_left,"o")
    # screen.onkey(move_snake_right,"p")




screen.exitonclick()