from turtle import *
import turtle

turtle.color("tan")

turtle.Screen().bgcolor("darkslateblue")

speed(100)
penup()
turtle.goto(0,200)
pendown()

for i in range (10):
    
    for i in range (6):

        for i in range (20):
            
            for i in range (5):
                forward(20)
                right(72)

            right(18)

        right(60)
        penup()
        forward(75)
        pendown()

    right(120)
    penup()
    forward(75)
    pendown()


