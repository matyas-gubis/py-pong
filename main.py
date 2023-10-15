import time
import turtle

from paddle import Paddle

screen = turtle.Screen()

screen.bgcolor("black")
screen.title("pong")
screen.setup(width=800, height=600)
move_up = False

screen.tracer(0)
player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
screen.update()
screen.listen()
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")
screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")

game_over = False
while not game_over:
    screen.update()

screen.exitonclick()
