from turtle import Screen
from player import Player
from car_manager import CarManager
from level import Level
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("The Turtle Crossing Capstone Game")

player = Player()
carmanager = CarManager()
level = Level()

screen.listen()
screen.onkey(player.up, "Up")

is_game_on = True
car_level = 0
car_loop = 0

while is_game_on:
    time.sleep(0.1)
    screen.update()
    level.get()
    if car_loop % 30 == 0:
        carmanager.create(car_level)
    carmanager.move(car_level)
    car_loop += 1
    
    # Detect collision with a car
    for c in carmanager.car_obj:
        i = c[0]
        if player.distance(i) < 20:
            is_game_on = False
            time.sleep(0.3)
            player.end()
            level.gameover()
            
    # Detect crossin end-line
    if player.ycor() >= 260:
        time.sleep(1)
        player.end()
        car_level += 1
        level.up()

screen.exitonclick()
