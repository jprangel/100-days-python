from turtle import Turtle, Screen

turtle = Turtle()

# Draw a square
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

screen = Screen()
screen.exitonclick()