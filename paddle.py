import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(starting_position)
        self.points = 0
        self.should_move_up = False
        self.should_move_down = False

    def turn_on_move_up(self):
        self.should_move_up = True

    def turn_on_move_down(self):
        self.should_move_down = True

    def stop(self):
        self.should_move_up = False
        self.should_move_down = False

    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 5)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 5)

    def score(self):
        self.points += 1


