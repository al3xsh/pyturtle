# intro_to_turtle.py
#
# author: alex shenfield
# date:   18/06/2025

from turtle import Turtle
from random import random

# create the turtle object
t = Turtle()
t.shape("turtle")

# set up the turtle
t.pensize(5)
t.pencolor("blue")

# set up the screen
my_screen = t.screen
my_screen.title("My Turtle Program")
my_screen.setup(width=1000, height=750, startx=0, starty=0)

# define the turtle's movement
for i in range(100):
    steps = int(random() * 25)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

# run the turtle
t.screen.mainloop()

