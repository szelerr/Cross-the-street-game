from turtle import Turtle

step = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.color('black')
        self.move_to_start()

    def up(self):
        new_y = self.ycor() + step
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() + -step
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - step
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + step
        self.goto(new_x, self.ycor())

    def move_to_start(self):
        self.goto(0, -280)