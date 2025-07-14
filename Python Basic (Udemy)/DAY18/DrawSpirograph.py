import turtle
from turtle import Turtle, Screen
import random


tim = Turtle()
turtle.colormode(255)

def generate_random_color() :
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    total_circles = int(360 / size_of_gap)
    for _ in range(total_circles):
        tim.color(generate_random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap) # heading function return the current direction of turtle, after we make shift in direction of turtle by 10(size_of_gap)

draw_spirograph(5)




screen = Screen()
screen.exitonclick()