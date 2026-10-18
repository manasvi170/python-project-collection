from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level :{self.score}",font=FONT)

    def level_up(self):
        self.score+=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)
