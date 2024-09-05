from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 50, 'normal')

class Scoreboard(Turtle):
    def __init__(self , x):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x, 230)
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self, player):
        self.goto(0,0)
        self.write(f"{player} Wins!", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)