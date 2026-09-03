import turtle as t
import random
from turtle import Screen
tim=t.Turtle()
t.colormode(255)
tim.speed(0)
def different_colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colour=(r,g,b)  #Tuple [Cant be changed in any case]
    return random_colour

# for _ in range(200):
#     tim.color(different_colors())
#     tim.circle(100)
#     tim.setheading(tim.heading() + 5)


#This version will make sure to draw that many circles that is needed
def draw_till_needed(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(different_colors())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_till_needed(size_of_gap=5)


screen=Screen()
screen.exitonclick()