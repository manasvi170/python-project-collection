from turtle import Turtle,Screen
screen=Screen()
X_AXIS=750  #width=800
Y_AXIS=550  #height=600
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("LightCyan3")
        self.shapesize(stretch_wid=1.2,stretch_len=1.2)
        self.x_move=10   #10 pixels
        self.y_move=10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed*=0.9


    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()



