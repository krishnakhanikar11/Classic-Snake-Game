from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.score = 0
        self.color('white')
        self.penup()
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
