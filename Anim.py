import turtle


#SETUP
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.title("Animee")
wn.bgcolor("Gray")
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)
pen.color("white")
pen.goto(-200, 0)


#ACTION
for i in range(5):
    pen.forward(500)
    pen.right(216)
    for i in range(5):
        pen.forward(200)
        pen.right(216)
        for i in range(5):
            pen.forward(75)
            pen.right(216)
            for i in range(5):
                pen.forward(25)
                pen.right(216)
turtle.done()