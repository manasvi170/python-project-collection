from turtle import Turtle,Screen
screen=Screen()
turtle=Turtle()
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=4,stretch_len=1)
        self.goto(position)

    def move_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)