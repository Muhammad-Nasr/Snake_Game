from turtle import Turtle



# make Constants
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y= 260)
        self.color("white")
        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score}     High score:{self.high_score}", align= ALIGNMENT, font= FONT)

    def write_score(self):
        self.score += 1
        self.update()

    def reset_game(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update()






