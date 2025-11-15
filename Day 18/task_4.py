import turtle as t
import random

tim = t.Turtle()
tim.width(7)

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def drunk_turtle():
    direction = random.randint(-1,1)
    tim.forward(10)
    tim.right(direction * 90)
    tim.speed(0)

for _ in range(100):
    tim.color(random.choice(colours))
    drunk_turtle()

screen = t.Screen()
screen.exitonclick()