from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",20,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.shape("blank") # or self.hideturtle()
        self.goto(0,250)
        self.update_score()


    def game_over(self):
        self.hideturtle()
        self.color("white")
        self.goto(0,0)  # or self.home()
        self.write("Game Over.",align=ALIGNMENT,font=FONT)


    def update_score(self):
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()



