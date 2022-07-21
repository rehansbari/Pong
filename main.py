from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Rehan's Pong Game")
screen.listen()
screen.tracer(0)

enemy_paddle = Paddle()
player_paddle = Paddle()
player_paddle.goto(-350, 0)
screen.onkey(player_paddle.up, "Up")
screen.onkey(player_paddle.down, "Down")
screen.onkey(enemy_paddle.up, "w")
screen.onkey(enemy_paddle.down, "s")
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detecting collision with the top and bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detecting collision with paddles
    if ball.distance(enemy_paddle) < 50 and ball.xcor() > 320 or ball.distance(player_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detecting when the ball has gone out of bounds
    #Detecting when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player_point()

    #Detecting when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.enemy_point()


screen.exitonclick()