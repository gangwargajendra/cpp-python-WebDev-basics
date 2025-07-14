import turtle
from turtle import Turtle, Screen
import  random

def generate_random_color() :
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)  # pyhton Tuple
    return random_color


tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)


tim.width(15)   #tim.pensize(15)
angles = [0, 90, 180, 270]

for _ in range (200) :
    tim.color(generate_random_color())
    tim.right(random.choice(angles))   # tim.setheading(random.choice(angles)
    tim.forward(30)




screen = Screen()
screen.exitonclick()