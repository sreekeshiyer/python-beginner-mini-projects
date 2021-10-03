from turtle import Turtle, Screen
import random
tt = Turtle()
tt.shape('turtle')

for i in range(3, 11):
    tt.color('#'+str(random.randint(100000, 999999)))
    for s in range(0, i):
        tt.forward(100)
        tt.right(360/i)


screen = Screen()
screen.exitonclick()
