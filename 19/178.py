# etch-a-sketch with turtle

from turtle import Turtle, Screen

tortoise = Turtle()
screen = Screen()


def move_forwards():
    tortoise.forward(10)


def move_backwards():
    tortoise.backward(10)


def turn_left():
    tortoise.left(10)


def turn_right():
    tortoise.right(10)


def pen_up():
    if tortoise.isdown():
        tortoise.penup()
    else:
        tortoise.pendown()


def clearAndHome():
    tortoise.clear()
    tortoise.penup()
    tortoise.home()
    tortoise.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="space", fun=pen_up)
screen.onkey(key="c", fun=clearAndHome)
screen.onkey(key="1", fun=lambda: tortoise.pencolor("black"))
screen.onkey(key="2", fun=lambda: tortoise.pencolor("red"))
screen.onkey(key="3", fun=lambda: tortoise.pencolor("orange"))
screen.onkey(key="4", fun=lambda: tortoise.pencolor("yellow"))
screen.onkey(key="5", fun=lambda: tortoise.pencolor("green"))
screen.onkey(key="6", fun=lambda: tortoise.pencolor("blue"))
screen.onkey(key="7", fun=lambda: tortoise.pencolor("purple"))
screen.exitonclick()
