from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f'Level: {self.score}', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(-80, 0)
        self.write('GAME OVER', font=('Arial', 20, 'normal'))
