from turtle import Turtle, Screen

turtle = Turtle()

# Draw a dot line
for _ in range(10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()