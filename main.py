import time
import turtle

from ball import Ball
from paddle import Paddle

screen = turtle.Screen()

screen.bgcolor("black")
screen.title("pong")
screen.setup(width=800, height=600)
move_up = False

screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
screen.update()
screen.listen()
screen.onkeypress(r_paddle.turn_on_move_up, "Up")
screen.onkeypress(r_paddle.turn_on_move_down, "Down")
screen.onkeypress(l_paddle.turn_on_move_up, "w")
screen.onkeypress(l_paddle.turn_on_move_down, "s")
screen.onkeyrelease(r_paddle.stop, "Up")
screen.onkeyrelease(r_paddle.stop, "Down")
screen.onkeyrelease(l_paddle.stop, "w")
screen.onkeyrelease(l_paddle.stop, "s")

game_over = False
while not game_over:
    time.sleep(0.01)
    ball.move()
    screen.update()
    ball.bounce_timer -= .01

    if l_paddle.should_move_up:
        l_paddle.move_up()

    if r_paddle.should_move_up:
        r_paddle.move_up()

    if l_paddle.should_move_down:
        l_paddle.move_down()

    if r_paddle.should_move_down:
        r_paddle.move_down()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and 330 < ball.xcor() < 360 \
            or ball.distance(l_paddle) < 50 and -330 > ball.xcor() > -360:
        ball.bounce_x()

    if ball.xcor() > 380:
        l_paddle.score()
        ball.restart()
        print(f"l_paddle score: {l_paddle.points} r_paddle score: {r_paddle.points}")

    if ball.xcor() < -380:
        r_paddle.score()
        ball.restart()
        print(f"l_paddle score: {l_paddle.points} r_paddle score: {r_paddle.points}")

screen.exitonclick()
