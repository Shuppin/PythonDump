import turtle


q = turtle.Turtle()
q.hideturtle()
q.speed(100)

turtle.bgcolor("azure")

q.goto(0,0)

q.pensize(1)

for i in range(6):

    q.begin_fill()
    q.color("khaki")

    for i in range(7):
        for i in range(2):
            q.circle(80,100)
            q.left(80)
        q.left(360/7)

    q.end_fill()

    q.begin_fill()
    q.color("peru")

    q.penup()
    q.goto(0,-40)
    q.pendown()

    q.circle(40)
    q.end_fill()

    q.speed(0)
    q.goto(0,0)
    q.pensize(1)
    q.color("black")

    def box123(length):
        for i in range(4):
            q.forward(length)
            q.right(90)

    for i in range(36):
        box123(10)
        box123(35)
        q.right(10)

q.right(60)
q.penup()
q.forward(75)
q.pendown()
        
        




