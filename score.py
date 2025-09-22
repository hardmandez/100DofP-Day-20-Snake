from turtle import Turtle

displayscore = Turtle()

class Score():
    def __init__(self):
        self.score = 0


    def displayscore(self):
        displayscore.clear()
        displayscore.penup()
        displayscore.color('green')
        displayscore.hideturtle()
        # t.goto(0,295)
        # t.write(str("Score"),align="center",font=("Arial",10,"bold"))
        displayscore.goto(0, 280)
        displayscore.write(str(self.score), align="center", font=("Arial", 10, "bold"))