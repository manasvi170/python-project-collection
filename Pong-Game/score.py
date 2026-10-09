from turtle import Turtle,Screen
screen=Screen()
FONT=("Courier",20,"normal")
ALIGNMENT="center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.shape("blank")
        self.l_score=0
        self.r_score=0
        self.update_score()

    def update_score(self):
        self.goto(-200, 250)
        self.write(f" 🫲 Score:{self.l_score}",align=ALIGNMENT,font=FONT)
        self.goto(200,250)
        self.write(f"Score:{self.r_score} 🫱",align=ALIGNMENT,font=FONT)

    def l_point(self):
        self.l_score+=1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score+=1
        self.clear()
        self.update_score()


    def game_over(self):
        self.write("Game Over",align=ALIGNMENT,font=FONT)
