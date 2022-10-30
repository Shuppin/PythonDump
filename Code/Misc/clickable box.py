import turtle
import time

turtle_size = 40
square_size = 150
click_delay = 0.05
counter = 0

box = turtle.Turtle("square")
screen = turtle.Screen()


def click_callback(x, y, box=box):
    if box.color()[0] == "Red":
        box.color("Green")
        time.sleep(click_delay)
        box.color("Red")
    else:
        box.color("Red")
        time.sleep(click_delay)
        box.color("Green")


#def setVal(val):
    #global globalVal
    #valueChanged = globalVal != val
    #if valueChanged:
    #    pass  # some function
    #globalVal = val
    #if valueChanged:
    #    pass  # some function


screen.setup(600, 200)
screen.title("Clickables!!")
screen.bgcolor("black")

box.shapesize(square_size / turtle_size)
box.color("Red")
box.penup()

while True:
    box.onclick(click_callback)
