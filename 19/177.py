from turtle import Turtle, Screen

tortoise = Turtle()
screen = Screen()


def move_forwards():
    tortoise.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()