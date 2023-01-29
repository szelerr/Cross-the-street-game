from turtle import Turtle
from random import choice, randrange

colors = ['red', 'orange', 'yellow']


class Car:

    def __init__(self):
        self.cars = []
        self.initialize_cars()
        self.draw_positions()

    def initialize_cars(self):
        for i in range(0, 20):
            car = Turtle()
            car.penup()
            car.shape('square')
            car.shapesize(1, 2)
            car.color(choice(colors))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - 10
            car.goto(new_x, car.ycor())

    def cycle_back(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto(310, car.ycor())

    def draw_positions(self):
        for car in self.cars:
            x = randrange(-280, 280)
            y = randrange(-240, 240, 30)
            car.goto(x, y)
