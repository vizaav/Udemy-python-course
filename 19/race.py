from turtle import Turtle, Screen
from random import randint


class MyTurtle:
    def __init__(self, color, shape="turtle", ):
        self.turtle = Turtle()
        self.turtle.color(color)
        self.turtle.shape(shape)
        self.turtle.speed(randint(1, 10))


screen = Screen()
screen.setup(width=screen.window_width(), height=screen.window_height())

screen.exitonclick()
