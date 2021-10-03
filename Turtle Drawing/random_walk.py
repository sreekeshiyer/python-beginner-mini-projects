from turtle import Turtle, Screen
import random
tt = Turtle()
tt.shape('turtle')
screen = Screen()
screen.colormode(255)

tt.pensize(15)
tt.speed("fastest")


def random_color():

    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


directions = [0, 90, 270]

for _ in range(300):
    tt.color(random_color())
    tt.forward(30)
    tt.setheading(random.choice(directions))


screen.exitonclick()
