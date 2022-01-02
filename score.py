from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 15, "normal")
G_FONT = ("courier", 25, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score {self.score}: High Score:{self.high_score}", align=ALIGNMENT, font=FONT)
        with open("Highest_score.txt", mode="w") as file:
            file.write(f"Highest Score = {self.high_score}")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()
