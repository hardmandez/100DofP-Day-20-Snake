from turtle import Screen, Turtle
import winsound
import pygame


screen = Screen()

class Snake():
    def __init__(self):
        self.snake_length = 3
        self.snake_start_x = 0
        self.snake_start_y = 0
        self.segment = []
        self.snake_position = []
        self.inbounds = True
        self.createsnake()
        self.movesnake()

    def createsnake(self):
        for _ in range(self.snake_length):
            self.new_snake_segment = Turtle(shape="square")
            self.new_snake_segment.penup()
            self.new_snake_segment.color("white")
            self.new_snake_segment.speed(0)
            self.new_snake_segment.goto(self.snake_start_x, self.snake_start_y)
            self.segment.append(self.new_snake_segment)
            self.snake_position.append((self.snake_start_x, self.snake_start_y))
            self.snake_start_x -= 20

    def movesnake(self):
        if self.inbounds == True:
            for seg_no in range(len(self.segment) - 1, 0, -1):
                self.segment
                new_x = self.segment[seg_no - 1].xcor()
                new_y = self.segment[seg_no - 1].ycor()
                self.segment[seg_no].goto(new_x, new_y)
            self.segment[0].forward(20)
            screen.update()

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
        # self.snake_position.append((self.snake_start_x, self.snake_start_y))
        # self.snake_start_x -= 20

    def checkcollision(self):
        for seg_no in range(1,len(self.segment)):
            if abs(self.segment[0].xcor() - self.segment[seg_no].xcor()) <= 2 and abs(self.segment[0].ycor() - self.segment[seg_no].ycor()) <= 2:
                return True
                # gameover = Turtle()
                # gameover.hideturtle()
                # gameover.color("red")
                # gameover.penup()
                # gameover.goto(0, 0)
                # gameover.write("GAME OVER", align="center", font=("Arial", 24, "bold"))


    def checkinbound(self):
        if self.segment[0].xcor() <= -300 or self.segment[0].xcor() >= 300 or self.segment[0].ycor() <= -300 or self.segment[0].ycor() >= 300:
            return True
            # self.inbounds = False
            # gameover = Turtle()
            # gameover.hideturtle()
            # gameover.color("red")
            # gameover.penup()
            # gameover.goto(0, 0)
            # gameover.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    def foodcollision(self, foodposition):
        snake_position = round(self.segment[0].xcor()), round(self.segment[0].ycor())
        food_position = foodposition
        if abs(snake_position[0] - food_position[0]) <= 15 and abs(snake_position[1] - food_position[1]) <= 15:
            pygame.mixer.init()
            pygame.mixer.music.load("apple-crunch.wav")
            pygame.mixer.music.play()

            self.addsegment()
            screen.update()
            # food.food_counter = 0
            # score.score += 1
            # # score.displayscore()
            return True