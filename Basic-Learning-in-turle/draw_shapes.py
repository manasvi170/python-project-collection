#draw shapes
from turtle import Turtle ,Screen
import random

Color=["black","HotPink2","OrangeRed","Gold","RoyalBlue","SteelBlue","Red","Purple"]
tim=Turtle()
tim.shape("classic")

def draw_shapes(side):
    angle=360/side
    for i in range(side):
        tim.right(angle)
        tim.forward(100)


for _ in range(3,11):
    tim.color(random.choice(Color))
    draw_shapes(_)


screen=Screen()
screen.exitonclick()