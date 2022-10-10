from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkeypress(fun=player.move, key="Up")

car_manager = CarManager()
scoreboard = Scoreboard()

car_speed = 0.1
is_game_on = True
while is_game_on:
    time.sleep(car_speed)
    screen.update()
    
    ###Creating new cars
    car_manager.create_car()
    
    ###Moving cars
    car_manager.go_left()
    
    ###Detecting car crash
    for car in car_manager.cars:
        if player.distance(car)<20:
            scoreboard.game_over()
            is_game_on = False
            
    ###Detecting if player crossed finish line
    if player.ycor() > 280:
        player.go_to_start()
        scoreboard.increase_level()
        #car_manager.level_up()
        car_speed *= 0.8
        
screen.exitonclick()