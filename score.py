from turtle import Turtle,Screen

screen = Screen()

displayscore = Turtle()

class Score():
    def __init__(self):
        self.score = 0
        self.foodbonus = 0
        self.speedboost = 0


    def displayscore(self):
        displayscore.clear()
        displayscore.penup()
        displayscore.color('green')
        displayscore.hideturtle()
        # t.goto(0,295)
        # t.write(str("Score"),align="center",font=("Arial",10,"bold"))
        displayscore.goto(0, 300)
        displayscore.write(f"Score: {self.score or 0}", align="center", font=("Arial", 10, "bold"))

    def boost_speed(self):
        self.speedboost +=1
        if self.speedboost == 2:
            self.speedboost = 0
            return True
    def update_score(self):
        self.score += 1
        self.displayscore()

    def food_bonus(self, food_counter):
        foodcounter = food_counter
        if self.foodbonus == 10:
            self.score += 10
            self.displayscore()
            self.foodbonus = 0
        elif foodcounter >= 1:
            self.foodbonus += 1
        print(self.foodbonus)

    def game_over(self):
        gameover = Turtle()
        gameover.hideturtle()
        gameover.color("red")
        gameover.penup()
        gameover.goto(0, 0)
        gameover.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        screen.update()


