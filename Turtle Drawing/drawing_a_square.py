from turtle import Turtle, Screen
from turtle import Turtle, Screen
tt = Turtle()
tt.shape('turtle')
tt.color('blue')

for i in range(0, 4):
    tt.forward(100)
    tt.right(90)


screen = Screen()
screen.exitonclick()
