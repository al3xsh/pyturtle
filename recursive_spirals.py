# recursive_spirals.py
#
# author: alex shenfield
# date:   18/06/2025

from turtle import Turtle, Screen
from turtle import done as turtle_done


# define the recursive spiral method
def spiral(input_len):
	if input_len <= 10:
		t.right(90)
	else:
		t.forward(input_len)
		t.left(90)
		spiral(input_len - 10)
		t.back(input_len)
		t.right(90)


# main program runs here ...

# set the turtle properties
t = Turtle()
t.shape("turtle")
t.speed("normal")
t.pensize(5)

# set the screen properties
s = Screen()
s.bgcolor("light gray")
s.title("Recursive Spirals")
s.setup(width=1000, height=750)

# run the drawing
for i in range(8):
	t.left(45)
	spiral(100)

# hide the turtle and wait for the window to be closed
t.hideturtle()
turtle_done()