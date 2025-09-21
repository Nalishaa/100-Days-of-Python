# Reeborg Escaping the Maze Solution
# Note: Requires Reeborg's World environment to run
# URL: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# This is my approach to solving the maze.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# Provided by the course
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()












