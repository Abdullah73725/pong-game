from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((400, 0))
l_paddle = Paddle((-400, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 or ball.xcor() > 410 or ball.distance(l_paddle) < 50 or ball.xcor() < -410:
        ball.bounce_x()

    #Detect R paddle missed the ball
    if ball.xcor() > 430:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle missed the ball
    if ball.xcor() < -430:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()