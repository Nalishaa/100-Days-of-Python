from turtle import Turtle,Screen
import random

colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

screen = Screen()
screen.setup(width=500,height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

offset = 0
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-75 + offset)
    offset = offset+25

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()