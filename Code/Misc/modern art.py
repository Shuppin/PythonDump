from turtle import *
from random import *
import turtle
colormode(255)

def randomcolour():
    
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)


def randomplace():
    penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
    pendown()

def randomheading():
    setheading(randint(1, 360))
    right(90)

def drawrectangle():
    hideturtle()
    lenght = randint(10, 100)
    height = randint(10, 100)
    begin_fill()
    forward(lenght)
    right(90)
    forward(height)
    right(90)
    forward(lenght)
    right(90)
    forward(height)
    right(90)
    end_fill()


def drawcircle():
    a = turtle.Turtle()
    q = randint(10, 100)
    begin_fill()
    a.circle(q)
    end_fill()
    
speed(0)



for i in range(5):
    hideturtle()
    randomcolour()
    randomplace()
    drawrectangle()
    #randomheading()
    stamp()

clear()

speed(0)

for i in range(100):
    randomcolour()
    randomplace()
    drawcircle()
    
    
    
