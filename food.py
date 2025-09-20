from turtle import Screen, Turtle
import random

class Snake():
    def __init__(self):
        self.food_start_x = 0
        self.food_start_y = 0
        # self.foodsegment = []
        self.foodposition = []
        self.createfood()

    def createfood(self):
        self.new_food_segment = Turtle(shape="circle")
        self.new_food_segment.penup()
        self.new_food_segment.color("green")
        self.food_start_x = random.randint(-290, 290)
        self.food_start_y = random.randint(-290, 290)
        self.new_food_segment.goto(self.snake_start_x, self.snake_start_y)
        self.segment.append(self.new_snake_segment)
        self.snake_position.append((self.snake_start_x, self.snake_start_y))
        self.snake_start_x -= 20

