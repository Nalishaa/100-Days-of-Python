# draw circle radius=100
# repeat and change tilt
# use random colors

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
for _ in range(72):
    tim.pensize(2)
    tim.speed(0)
    tim.color(random_color())
    tim.hideturtle()
    tim.circle(100)
    tim.left(5)

screen = t.Screen()
screen.exitonclick()