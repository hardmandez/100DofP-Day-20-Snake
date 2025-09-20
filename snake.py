from turtle import Screen, Turtle

class Snake():
    def __init__(self):
        self.snake_length = 3
        self.snake_start_x = 0
        self.snake_start_y = 0
        self.segment = []
        self.snake_position = []
        self.createsnake()
        self.movesnake()

    def createsnake(self):
        for _ in range(self.snake_length):
            self.new_snake_segment = Turtle(shape="square")
            self.new_snake_segment.penup()
            self.new_snake_segment.color("white")
            self.new_snake_segment.goto(self.snake_start_x, self.snake_start_y)
            self.segment.append(self.new_snake_segment)
            self.snake_position.append((self.snake_start_x, self.snake_start_y))
            self.snake_start_x -= 20

    def movesnake(self):
        for seg_no in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_no - 1].xcor()
            new_y = self.segment[seg_no - 1].ycor()
            self.segment[seg_no].goto(new_x, new_y)
        self.segment[0].forward(20)

    def movesnakeleft(self):
        self.segment[0].left(90)
        # self.segment[0].forward(20)

    def movesnakeright(self):
        self.segment[0].right(90)
        # self.segment[0].forward(20)

    def addsegment(self):
        self.new_snake_segment = Turtle(shape="square")
        self.new_snake_segment.penup()
        self.new_snake_segment.color("white")
        self.new_snake_segment.goto(self.snake_start_x, self.snake_start_y)
        self.segment.append(self.new_snake_segment)
        self.snake_position.append((self.snake_start_x, self.snake_start_y))
        self.snake_start_x -= 20


