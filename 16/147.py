import another_module
print(another_module.another_variable)
def draw_arm(turtle):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(20)

def draw_flower(turtle):
    for _ in range(36):
        draw_arm(turtle)
        turtle.right(10)


def draw_flower2(turtle):
    for _ in range(20):
        turtle.forward(100)
        turtle.right(100)
        turtle.forward(100)
        turtle.right(100)
        turtle.forward(100)
        turtle.right(100)
        turtle.forward(100)
        turtle.left(100)


from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.speed("fastest")
my_screen = Screen()
print(my_screen.canvheight)
for _ in range(10):
    draw_arm(timmy)
    timmy.right(40)
draw_flower(timmy)
draw_flower2(timmy)

my_screen.exitonclick()

