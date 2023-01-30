from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def turn_left():
    turtle.left(10)

def turn_right():
    turtle.right(10)

def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    welcome()

def welcome():
    turtle.penup()
    turtle.hideturtle()
    turtle.setposition(-250.0, 300.0)
    turtle.write("Commands = \n Key W to move Forward\n Key S to move Backward\n", True, align="right")
    turtle.setposition(-220.0, 280.00)
    turtle.write("Key A to turn Left\nKey S to turn Right\nKey C to Clean", True, align="right")
    turtle.home()
    turtle.showturtle()

def start():
    welcome()
    turtle.pendown()
    screen.listen()
    screen.onkey(move_forward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear_screen, "c")
    screen.exitonclick()

start()
