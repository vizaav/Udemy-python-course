from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall.
    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            




screen.exitonclick()
