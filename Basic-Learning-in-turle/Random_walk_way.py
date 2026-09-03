import turtle as t
from turtle import Screen
import random
tim=t.Turtle()
t.colormode(255)

# Color=["black","HotPink2","OrangeRed","Gold","RoyalBlue","SteelBlue","Red","Purple",
#        "red", "green", "blue", "yellow", "magenta", "cyan", "orange", "purple", "pink", "brown",
#        "black", "white", "gray", "darkgray", "lightgray", "whitesmoke",
#        "navy", "skyblue", "darkblue", "royalblue", "deepskyblue", "turquoise",
#        "lightgreen", "darkgreen", "forestgreen", "olive", "seagreen", "gold", "maroon",
#        "violet", "salmon", "chocolate", "coral", "beige"]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return random_color



direction=[0,90,180,270]
tim.speed(10)
tim.pensize(10)
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen=Screen()
screen.exitonclick()