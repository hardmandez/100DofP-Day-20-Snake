from turtle import Screen, Turtle

screen = Screen()
turtle = Turtle()
def introscreen():
    turtle.pencolor("green")
    turtle.penup()
    turtle.hideturtle()
    turtle.pensize(width=1)
    turtle.goto(-300,-300)
    turtle.setheading(90)
    turtle.pendown()
    for side in range(4):
        turtle.forward(600)
        turtle.right(90)
    turtle.penup()
    turtle.goto(-300,300)
    turtle.write("Grub", align="Left", font=("Arial", 10, "bold"))
    turtle.goto(300, 300)
    turtle.write("Ranking", align="Right", font=("Arial", 10, "bold"))

def introscreen():
    turtle.pencolor("green")
    turtle.penup()
    turtle.hideturtle()
    turtle.pensize(width=1)
    turtle.goto(-300,-300)
    turtle.setheading(90)
    turtle.pendown()
    for side in range(4):
        turtle.forward(600)
        turtle.right(90)
    turtle.penup()
    turtle.goto(-300,300)
    turtle.write("The Grub", align="Left", font=("Arial", 10, "bold"))
    turtle.goto(300, 300)
    turtle.write("Ranking", align="Right", font=("Arial", 10, "bold"))
