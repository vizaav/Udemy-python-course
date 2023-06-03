import turtle as t
import random

colors = ["green", "blue", "red", "orange", "purple", "pink", "cyan"]
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.goto(0, -200)
tim.pendown()


def draw_shape(num_sides):
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(360 / num_sides)


for shape_side_n in range(3, 20):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
