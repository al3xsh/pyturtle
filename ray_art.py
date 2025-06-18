# ray_art.py
#
# author: alex shenfield
# date:   18/06/2025

from turtle import Turtle
from turtle import Screen
import random
import time

# i have built a ray class to draw indivdual rays using a new turtle each time
class Ray():

    # set the colours to cycle through
    colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']

    def __init__(self, pensize):

        # set up the turtle for drawing this ray
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.setpos(0, 0)

        # set the colour and size of the turtle pen
        index = random.randint(0, len(self.colors) - 1)
        self.turtle.pencolor(self.colors[index])
        self.turtle.speed('fastest')
        self.turtle.pensize(pensize)

    # draw the two part ray
    def draw(self):

        # draw the main bit of the ray
        heading = random.randint(0, 360)
        self.turtle.setheading(heading)
        self.turtle.forward(random.randint(15, 150))

        # draw the head of the ray
        heading += random.randint(-35, 35)
        self.turtle.setheading(heading)
        self.turtle.forward(random.randint(15, 150))


# test case
if __name__ == "__main__":

    # set up the screen
    my_screen = Screen()
    my_screen.title("Colourful Rays")
    my_screen.setup(width=1000, height=750)
    my_screen.bgcolor("light gray")

    # total number of rays of each thickness to draw
    num_rays = 5

    # start at 25 and reduce the size by one after each num_rays has been drawn
    for size in range(25, 0, -1):

        for n_ray in range(num_rays):

            ray = Ray(size)
            ray.draw()
            time.sleep(0.1)

            print("line size: " + str(size))

    # leave the picture on the screen until it's clicked
    print("click on the window to exit")
    my_screen.exitonclick()

    