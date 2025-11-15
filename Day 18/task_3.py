from turtle import Turtle, Screen
timmy = Turtle()
timmy.width(5)
colors = ["red","orange","yellow","green","blue","cyan4","DeepPink4","DarkOrchid4"]
side = 3
shade = 0

while side <= 10:
    timmy.color(colors[shade])
    angle = 360/side
    i = side
    while i > 0:
        timmy.forward(100)
        timmy.right(angle)
        i = i-1
    side = side+1
    shade = shade+1


screen = Screen()
screen.exitonclick()