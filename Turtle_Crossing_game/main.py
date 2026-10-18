# default width=360(720) or 370(740) height =300(600)
import time
from turtle import Screen
from player import Player
from cars import Car
from score import Scoreboard

screen = Screen()
screen.title("Turtle crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
cars = Car()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

    # Detect collision of turtle with car
    for car in cars.all_cars:
        if car.distance(player)<25:
            game_is_on=False
            score.game_over()

    # Turtle crossed the path(won)
    if player.is_at_goal():
        player.at_starting()
        cars.increase_speed()
        score.level_up()

screen.exitonclick()
