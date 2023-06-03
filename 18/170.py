import random
import turtle

turtle.colormode(255)


def draw_randomly(timmy):
    def random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    while True:
        timmy.color(random_color())
        timmy.forward(20)
        timmy.left(random.choice([0, 90, 180, 270]))


timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.pensize(10)
timmy.speed("fastest")
draw_randomly(timmy)
