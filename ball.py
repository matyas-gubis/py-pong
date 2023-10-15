import time
from random import random, Random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed_multiplier = 3
        self.bounce_timer = 0
        self.color("white")
        self.shape("circle")
        self.penup()
        self.up_speed = 1
        self.right_speed = 1
        # self.generate_move_vector()
        # self.move()

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.up_speed *= -1

        self.goto(self.xcor() + self.right_speed * self.speed_multiplier,
                  self.ycor() + self.up_speed * self.speed_multiplier)

    def bounce_x(self):
        if self.bounce_timer < 0:
            self.bounce_timer = .5
            self.right_speed *= -1

    def restart(self):
        self.goto(0, 0)
        self.speed_multiplier = 3

    # def generate_move_vector(self):
    #     self.move_vector = ()
    def increase_speed(self):
        self.speed_multiplier += .1


