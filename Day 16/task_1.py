# import turtle
#
# timmy = turtle.Turtle()
# # object       # class
# print(timmy)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")     # shape, color, etc. are methods
timmy.color("chartreuse3")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)  # canvheight is an attribute
my_screen.exitonclick()
