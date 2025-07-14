### the commented code will generate color_list using a image
### by colorgram, we can extract color from an image
import turtle
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('./image.jpg', 30)
#
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

###### from here our project will start

from turtle import Turtle, Screen
import random

def method_1() :
    tim = Turtle()
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    turtle.colormode(255)  # it makes that turtle can take rgb color value as parameter

    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

    x_coordinate = -240
    y_coordinate = -240

    for _ in range(10) :
        y_coordinate += 50
        tim.setposition((x_coordinate, y_coordinate))
        for _ in range(10) :
            tim.dot(20, random.choice(color_list))
            tim.forward(50)


def method_2() :
    turtle.colormode(255)
    tim = Turtle()
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()

    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
                  (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
                  (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
                  (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
                  (107, 127, 153), (174, 94, 97), (176, 192, 209)]

    tim.setheading(225)  # now turtle will point in middle of 180 and 270 which is middle of third quadrant
    tim.forward(300)
    tim.setheading(0)
    number_of_dots = 100

    for dot_count in range(1 , number_of_dots + 1) :
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0 :
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


method_2()


screen = Screen()
screen.exitonclick()