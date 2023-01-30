import turtle as t
import random

turtle = t.Turtle()
screen = t.Screen()
screen.colormode(255)
turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


a = 5
t = int(360/5)

for i in range(t):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.right(a)

screen.exitonclick()
