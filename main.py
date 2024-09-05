from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH , height=HEIGHT)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score_1 = Scoreboard(-50)
score_2 = Scoreboard(50)

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor()>320 or ball.distance(l_paddle) < 50 and ball.xcor()<-320 :
        ball.paddle()

    if ball.xcor() > 380:
        score_1.update()
        ball.reset_position()

    if ball.xcor() < -380:
        score_2.update()
        ball.reset_position()

    if score_1.score == 10 :
        score_1.game_over("Left Player")
        game_is_on = False
    elif score_2.score == 10:
        score_1.game_over("Right Player")
        game_is_on = False

screen.exitonclick()