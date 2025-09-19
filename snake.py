from turtle import Screen, Turtle

def ___init___():
    snake_length = 5
    snake_start_x = 0
    snake_start_y = 0
    segment = []
    snake_position = []


def move():
    for _ in range(snake_length):
        new_snake_segment = Turtle(shape="square")
        new_snake_segment.penup()
        new_snake_segment.color("white")
        # new_snake_segment.speed("fastest")
        new_snake_segment.goto(snake_start_x, snake_start_y)
        segment.append(new_snake_segment)
        snake_position.append((self.snake_start_x, self.snake_start_x))
        snake_start_x -= 20