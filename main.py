from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import intro

import time

new_game = True
game_on = True
snake_speed = 0.2
my_snake = Snake()
food = Food()
score = Score()

#Define screen.
screen = Screen()
screen.setup(width=635, height=635,startx=None, starty=5)
screen.bgcolor("black")
screen.title("The Grub")
screen.tracer(0)
score.displayscore()

screen.listen()
intro.introscreen()
# screen.onkey(game_loop, "")
screen.onkey(my_snake.movesnakeleft,"Left")
screen.onkey(my_snake.movesnakeright,"Right")

#Game Loop
# def game_loop():
while game_on:
    while new_game:
        screen.update()
        time.sleep(snake_speed)
        my_snake.movesnake()
        food.createfood()

        # Check for food collision.
        detectfoodcollision = my_snake.foodcollision(food.food_position)
        if detectfoodcollision:
            #Update score.
            score.update_score()

            if food.food_counter > 0:
                score.food_bonus(food.food_counter)

            #Reset food counter to create new item.
            food.food_counter = 0

            #Increase speed if meet score threshold.
            increase_speed = score.boost_speed()

            if increase_speed and snake_speed > 0.01:
                snake_speed -= 0.01


        #Detect increase sped


        # Check for snake collision.
        detectsnakecollision = my_snake.checkcollision()
        if detectsnakecollision:
            score.game_over()
            new_game = False

        #Check for out of screen.
        detectoutofbounds = my_snake.checkinbound()
        if detectoutofbounds:
            score.game_over()
            new_game = False


    # play_again = input("Would you like to play again? (y/n) ")
    # if play_again == "y":
    #     new_game = True
    #     turtle.reset()
    #     turtle.clear()

# screen.exitonclick()
turtle.mainloop()