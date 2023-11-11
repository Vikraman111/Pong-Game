from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.create_paddle()
        self.goto(x=x_pos, y=y_pos)

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)