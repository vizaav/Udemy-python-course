from turtle import Turtle, Screen
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
is_race_on = False


class MyTurtle(Turtle):
    def __init__(self, color, shape="turtle"):
        super().__init__()
        self.color(color)
        self.shape(shape)
        self.speed(5)

    def changeSpeed(self, speed):
        self.speed(speed)


# prepare the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Need for Speed - Nintendo Edition")
screen.bgcolor("black")

# get user bet
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = ""
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet not in colors:
        # print a message to the screen
        print("Please enter a valid color.")
y_positions = [-SCREEN_HEIGHT / 4, -SCREEN_HEIGHT / 8, 0, SCREEN_HEIGHT / 8, SCREEN_HEIGHT / 4]

if user_bet:
    is_race_on = True

# create 5 turtles
all_turtles = []
for i in range(0, 5):
    new_turtle = MyTurtle(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-SCREEN_WIDTH / 2 + 10, y=y_positions[i])
    new_turtle.pendown()
    all_turtles.append(new_turtle)

# start the race

winner = ""

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= SCREEN_WIDTH / 2 - 10:
            is_race_on = False
            winner = turtle.pencolor()

# print the winner
if winner == user_bet:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")

screen.exitonclick()
