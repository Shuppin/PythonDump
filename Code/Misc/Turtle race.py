from turtle import *
from random import randint

speed(0)
penup()
goto(-340, 140)
distance = 1000

for step in range(40):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-360, 100)
ada.right(360)
ada.pendown()


bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-360, 70)
bob.right(360)
bob.pendown()


laz = Turtle()
laz.color('green')
laz.shape('turtle')

laz.penup()
laz.goto(-360, 40)
laz.left(360)
laz.pendown()


leo = Turtle()
leo.color('yellow')
leo.shape('turtle')

leo.penup()
leo.goto(-360, 10)
leo.left(360)
leo.pendown()



for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    laz.forward(randint(1,5))
    leo.forward(randint(1,5))
    

    
    
 
