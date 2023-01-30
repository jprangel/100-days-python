from turtle import Turtle, Screen

turtle = Turtle()

# Draw from triangle, square, pentagon, hexagon
# heptagon, octagon, nonagon and decagon in diff colors.
sides = 3
colors = ["blue", "green", "red", "brown", "orange", "purple", "black", "magenta", "medium turquoise",
         "olive drab", "peru", "firebrick", "medium violet red", "indigo", "slate blue", "pale violet red",
         "saddle brown", "dodger blue", "slate gray"]

for i in range(8):
    turtle.color(colors[i])
    for s in range(sides):
        angle = 360 / sides
        turtle.forward(100)
        turtle.right(angle)
    sides += 1

screen = Screen()
screen.exitonclick()
