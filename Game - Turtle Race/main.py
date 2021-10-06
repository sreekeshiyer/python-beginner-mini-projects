from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=600)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

user_choice = (screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")).lower()


for i in range(0, 6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-380, y=(5-2*i)*25)

if user_choice in colors:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 370:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_choice:
                print(
                    f"You've won! The {winner.title()} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winner.title()} turtle is the winner!")
        random_distance = random.randint(10, 20)
        turtle.forward(random_distance)


screen.exitonclick()
