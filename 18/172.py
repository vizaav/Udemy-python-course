import turtle
import random

turtle.colormode(255)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_circles(timmy, radius=360):
    if radius <= 0:
        return
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(10)
    radius -= 10
    draw_circles(timmy, radius)


timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
draw_circles(timmy)

screen = turtle.Screen()
screen.exitonclick()
