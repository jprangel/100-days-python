import colorgram
import turtle as t
import random

# Create Hirst painting 10 x 10, dot size 20, 50 space

turtle = t.Turtle()
screen = t.Screen()

turtle.hideturtle()
screen.colormode(255)
turtle.speed("fastest")
num_colors = 20
colors = colorgram.extract('image.jpg', num_colors)
my_colors = []
space = 50
dot_size = 20
x = -230.00
y = -230.00

turtle.penup()
turtle.setposition(x, y)
turtle.pendown()

for c in range(len(colors)):
    rgb = colors[c].rgb
    my_rgb = (rgb[0], rgb[1], rgb[2])
    my_colors.append(my_rgb)


def random_color():
    color = random.choice(my_colors)
    return color


for i in range(10):
    for d in range(10):
        turtle.pendown()
        turtle.dot(dot_size, random_color())
        turtle.penup()
        turtle.fd(space)
    y += space
    turtle.setposition(x, y)

screen.exitonclick()
