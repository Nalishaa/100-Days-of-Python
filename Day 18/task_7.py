# import colorgram
#
# colors_list = []
# all_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     colors_list.append(color.rgb)
#
# for item in colors_list:
#     r = item[0]
#     g = item[1]
#     b = item[2]
#     rgb = (r,g,b)
#     all_colors.append(rgb)


# 10 x 10 rows of spots
# size of dots = 5
# spaced apart by 50 paces
import turtle as t
import random
screen = t.Screen()
tim = t.Turtle()
colors_list = [ (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.hideturtle()
t.colormode(255)
x = -screen.window_width()/2
y = -screen.window_height()/2
tim.teleport(x,y)
tim.speed(0)

for i in range(10):
    for j in range(10):
        color = random.choice(colors_list)
        tim.dot(20,color)
        tim.penup()
        tim.forward(50)
    y = y+50
    tim.teleport(x,y)

screen.exitonclick()


