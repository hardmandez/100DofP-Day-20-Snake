from turtle import Screen, Turtle

class Snake():
    def __init__(self):
        self.snake_length = 5
        self.snake_start_x = 0
        self.snake_start_y = 0
        self.segment = []
        self.snake_position = []
        self.createsnake()

    def createsnake(self):
        for _ in range(self.snake_length):
            self.new_snake_segment = Turtle(shape="square")
            self.new_snake_segment.penup()
            self.new_snake_segment.color("white")
            self.new_snake_segment.goto(self.snake_start_x, self.snake_start_y)
            self.segment.append(self.new_snake_segment)
            self.snake_position.append((self.snake_start_x, self.snake_start_y))
            self.snake_start_x -= 20

    def MoveSnake(self):
       return
