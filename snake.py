# create a snake class include every thing about the snake
from turtle import Turtle

snake_positions = [(0, 0), (-20, 0), (-40, 0)]


UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for position in snake_positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_segments.append(snake_part)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):

        for seg_num in range(len(self.snake_segments) - 1, 0, -1):  # range (start = , stop = , step = )
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x=new_x, y=new_y)

        self.snake_head.forward(20)

    def snake_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def snake_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def snake_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def snake_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def reset_game(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)

        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]






