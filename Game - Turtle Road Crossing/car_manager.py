from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        if random.randint(1, 6) in [1]:
            car = Turtle(shape="square")
            car.pu()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(x=300, y=random.randint(-250, 250))
            self.cars.append(car)
        
    def go_left(self):
        for car in self.cars:
            car.goto(x=(car.xcor()-self.car_speed), y=car.ycor())   # Place car at random start point
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT    # Increase car speed