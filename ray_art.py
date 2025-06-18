# ray_art.py
#
# author: alex shenfield
# date:   18/06/2025

from turtle import Turtle
from turtle import Screen
import random
import time


class Ray():

    # set the colours to cycle through
    colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']

    def __init__(self, pensize):

        # set up the turtle for drawing this ray
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.setpos(0, 0)
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


    count = 0
    size = 25
    while True:
        count += 1
        if count % 5 == 0 and size != 1:
            size -= 1
        if size == 1:
            print("Only drawing small lines now")
        print("line size: " + str(size))

        ray = Ray(size)
        ray.draw()
        time.sleep(0.1)



    # count = 0
    # size = 25
    # while True:
    #     try:
    #         count += 1
    #         if count % 5 == 0 and size != 1:
    #             size -= 1
    #         if size == 1:
    #             print("Only drawing small lines now")
    #         print("line size: " + str(size))

    #         newFormed = Ray(t, size)
    #         newFormed.draw()
    #         time.sleep(0.1)

    #     except KeyboardInterrupt:
    #         my_screen.done()

    