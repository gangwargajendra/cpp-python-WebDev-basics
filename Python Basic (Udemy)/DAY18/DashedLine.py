from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15) :
    tim.forward(5)
    tim.color("white")  #tim.penup()
    tim.forward(5)
    tim.color("black")  #tim.pendown()

screen = Screen()
screen.exitonclick()