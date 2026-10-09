# creating a pong game
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.title("Pong")

screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Working of left paddle
right_paddle = Paddle((350, 0))
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

ball = Ball()
score=Score()

# Working of left paddle
left_paddle = Paddle((-350, 0))
screen.onkey(left_paddle.move_up, "u")
screen.onkey(left_paddle.move_down, "d")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce the ball
        ball.bounce_y()

    #Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        if ball.distance(right_paddle) < 50:
            score.r_point()
        elif ball.distance(left_paddle) < 50:
            score.l_point()
        ball.bounce_x()

    # When Right paddle misses
    if ball.xcor() >380:
        ball.reset_position()
        score.l_point()

    # When Left paddle misses
    if ball.xcor() <-380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()