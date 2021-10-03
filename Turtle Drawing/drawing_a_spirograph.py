from turtle import Turtle, Screen
import random

tt = Turtle()
screen = Screen()
screen.colormode(255)
tt.speed("fastest")


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


i = 5
tt.setheading(10)
while tt.heading() != 0.0:
    tt.color(random_color())
    tt.circle(100)
    tt.setheading(i)
    i += 5

screen.exitonclick()
