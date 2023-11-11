from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.print_score()

    def print_score(self):
        self.goto(x=-100, y=200)
        self.write(arg=self.left_score, align=ALIGN, font=FONT)
        self.setx(100)
        self.write(arg=self.right_score, align=ALIGN, font=FONT)

    def update_score(self, player):
        if player == "right":
            self.right_score += 1
        elif player == "left":
            self.left_score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", align=ALIGN, font=FONT)