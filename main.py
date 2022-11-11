from turtle import Screen
from paddle import Paddle
from ball import Ball
from screenboard import Screenboard
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screenboard = Screenboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    # detect collision with top_down wall
    if ball.ycor() > 270 or ball.ycor() < - 270:
        ball.y_bounce()

    # detect collision with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.x_bounce()

    # detect r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        screenboard.update_left_score()

    # detect l_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        screenboard.update_right_score()


screen.exitonclick()
