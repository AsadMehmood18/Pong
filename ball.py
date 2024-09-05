from turtle import Turtle

SPEED = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.middle_line()
        self.move_speed = 0.1

    def middle_line(self):
        y = 290
        self.goto(0, y)
        self.setheading(270)
        while y>-290:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
            y-=20
        self.goto(0,0)
        self.setheading(0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle(self):
        self.x_move *= -1
        self.move_speed *=0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.paddle()
