from turtle import Turtle, Screen, numinput
import random

rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197,
                                                                                                                                                                                                   92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148,
                                                                                                                                                                                                                                                                                                                                                                                     129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]


tt = Turtle()
screen = Screen()
screen.colormode(255)
tt.speed("fastest")
tt.penup()
tt.hideturtle()
tt.setheading(135)
tt.forward(300)
tt.setheading(0)

tt.dot(20, random.choice(rgb_colors))

num_of_dots = 100

for count in range(1, num_of_dots+1):
    tt.dot(20, random.choice(rgb_colors))
    tt.forward(50)

    if count % 10 == 0 and count != 100:
        tt.setheading(270)
        tt.forward(50)
        tt.setheading(180)
        tt.forward(500)
        tt.setheading(0)

screen.exitonclick()
