from turtle import Turtle, Screen
tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)
def turn_up():
    tim.setheading(90)
    tim.forward(10)

def move_down():
    tim.setheading(270)
    tim.forward(10)
def turn_left():
    tim.setheading(180)
    tim.forward(10)
def turn_right():
    tim.setheading(0)
    tim.forward(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def counter_clockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def backward():
    tim.backward(10)
screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.onkey(key="Up",fun=turn_up)
screen.onkey(key="Down",fun=move_down)
screen.onkey(key="Left",fun=turn_left)
screen.onkey(key="Right",fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="b",fun=backward)

screen.exitonclick()