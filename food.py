# create new class inherited from turtle class
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()     # initialize every thing from the turtle class
        self.shape("circle")
        self.penup()
        self.color("purple")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        self.goto(x=x_random, y=y_random)



