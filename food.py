from turtle import Screen, Turtle
import time
import random

class Food():
    def __init__(self):
        self.food_start_x = 0
        self.food_start_y = 0
        # self.food_segment = []
        # self.food_position = []
        self.food_counter = 0
        self.new_food_segment = Turtle(shape="circle")
        self.new_food_segment.penup()
        self.new_food_segment.color("green")
        # self.new_food_segment.shapesize(stretch_wid=0.1, stretch_len=0.1)

    def createfood(self):
        if self.food_counter == 0:
            self.food_start_x = random.randrange(-290, 290, 10)
            self.food_start_y = random.randrange(-290, 290, 10)
            self.new_food_segment.goto(self.food_start_x, self.food_start_y)
            self.food_segment = (self.new_food_segment)
            self.food_position = ((self.food_start_x, self.food_start_y))
            self.food_counter = 50
        else:
            self.food_counter -= 1


