from turtle import Screen
from car import Car
from player import Player
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = Car()
player = Player()
scoreboard = Scoreboard()
game_speed = 0.1

screen.listen()
screen.onkeypress(player.up, 'Up')
screen.onkeypress(player.down, 'Down')
screen.onkeypress(player.move_left, 'Left')
screen.onkeypress(player.move_right, 'Right')

is_game_on = True

while is_game_on:
    time.sleep(game_speed)
    screen.update()

    car.move()
    car.cycle_back()

    if player.ycor() == 280:
        player.move_to_start()
        scoreboard.update_scoreboard()
        car.draw_positions()
        game_speed *= 0.9

    for obstacle in car.cars:
        if player.distance(obstacle) < 20:
            is_game_on = False


scoreboard.game_over()

screen.exitonclick()
