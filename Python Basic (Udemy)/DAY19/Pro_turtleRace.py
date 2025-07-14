import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
turtle_list = []

for turtle_index in range(0, 6) :
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-220, y=-125 + turtle_index * 50)
    turtle_list.append(new_turtle)


if user_bet :
    is_race_on = True

while is_race_on :
    selected_turtle = random.choice(turtle_list)
    turtle_step = random.randint(0 , 10)
    selected_turtle.forward(turtle_step)
    if selected_turtle.xcor() >= 220 :
        is_race_on = False
        winner_turtle_color = selected_turtle.pencolor()
        if winner_turtle_color.lower() == user_bet.lower() :
            print(f"You've won! The {winner_turtle_color} turtle is the winner.")
        else :
            print(f"You've lost! The {winner_turtle_color} turtle is the winner.")


screen.exitonclick()