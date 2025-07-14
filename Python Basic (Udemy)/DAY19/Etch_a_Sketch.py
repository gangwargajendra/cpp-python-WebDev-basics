from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)
    ####   OR    ####
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)

def turn_right():
    tim.right(10)

def clear_drawing():
    tim.clear()  # it's delete only this turtle drawing.
    # screen.clear()  # it's delete all including the turtle.
    tim.penup()
    tim.home()  # it will make turtle again at origin(0,0)
    tim.pendown()

screen.listen()   # it set up the screen to listen for keyboard
screen.onkey(key="w", fun=move_forward)  # on pressing key(w), fun(function) will run once
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
