import turtle as t
import random

turtle = t.Turtle()
screen = t.Screen()

# Draw a random walk multi-color with a tick line and speed the turtle.

# Random RGB colors
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_random = (r, g, b)
    return color_random

# Predefined colors
colors = ["blue", "green", "red", "brown", "orange", "purple", "black", "magenta", "medium turquoise",
         "olive drab", "peru", "firebrick", "medium violet red", "indigo", "slate blue", "pale violet red",
         "saddle brown", "dodger blue", "slate gray"]

sides = [0, 90, 180, 270]
turtle.speed("fast")
turtle.pensize(15)
space = 50


def drawline():
    turtle.color(random_color())
#    turtle.color(random.choice(colors))
    turtle.setheading(random.choice(sides))
    turtle.forward(30)


for i in range(50):
    drawline()


screen.exitonclick()
