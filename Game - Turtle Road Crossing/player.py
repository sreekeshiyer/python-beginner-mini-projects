from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.seth(90)
        self.go_to_start()
        
    def move(self):
        self.fd(MOVE_DISTANCE)  # Move turtle a set amount when function is called
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)    # Reset turtle position to start