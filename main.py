## Build a snake game

# import data

from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()

screen.bgcolor("black")  # background
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.tracer(0)



snake = Snake()
food = Food()
score_board = ScoreBoard()

# construct methods to use keys
screen.listen()
screen.onkey(fun=snake.snake_up, key="Up")
screen.onkey(fun=snake.snake_right, key="Right")
screen.onkey(fun=snake.snake_down, key="Down")
screen.onkey(fun=snake.snake_left, key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    if snake.snake_head.distance(food) < 18:
        snake.extend()
        food.refresh()
        score_board.write_score()

    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 299 or snake.snake_head.ycor() < -300:

        score_board.reset_game()
        snake.reset_game()

    for segment in snake.snake_segments[1:]:

        if snake.snake_head.distance(segment) < 10:
            game_is_on = False







screen.exitonclick()
