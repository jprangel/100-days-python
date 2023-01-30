from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=800, height=600)

turtle_list = ["pink", "purple", "blue", "green", "red", "orange", "yellow"]
turtle_obj = []
turtle_position = [-90, -60, -30, 0, 30, 60, 90]
x_start = -370.0
x_end = 350
speedway_h = 250
speedway_w = 740
is_race_on = False

def init():
    i = 0
    for t in turtle_list:
        t = Turtle()
        turtle_tuples = (t, turtle_list[i])
        turtle_obj.append(turtle_tuples)
        i += 1

def speedway():
    turtle = Turtle()
    turtle.penup()
    turtle.setposition(x=x_start, y=120)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(speedway_h)
    turtle.setheading(0)
    turtle.forward(speedway_w)
    turtle.setheading(90)
    turtle.forward(speedway_h)
    turtle.setheading(180)
    turtle.forward(speedway_w)

def def_shape_color():
    for t in turtle_obj:
        t[0].shape("turtle")
        t[0].color(t[1])

def ready_position():
    i = 0
    for t in turtle_obj:
        t[0].penup()
        t[0].goto(x_start, turtle_position[i])
        i += 1

def user_bet():
    global user_bet_op
    option_valid = False
    while not option_valid:
        user_bet_op = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (blue, green, red, orange, yellow, pink or purple)")
        if user_bet_op in turtle_list:
            option_valid = True
        else:
            print("Option Invalid")

def start():
    user_bet()
    speedway()
    init()
    def_shape_color()
    ready_position()
    if user_bet:
        is_race_on = True
    while is_race_on:
        for t in turtle_obj:
            t[0].forward(random.randint(0,10))
            pos = round(t[0].xcor(), 0)
            if pos > x_end:
                is_race_on = False
                print(f"The WINNER is... {t[1]} !!!")
                if user_bet_op.lower() != t[1]:
                    print(f"You lose, you choosed {user_bet_op} and the WINNER is {t[1]}")
                else:
                    print(f"You beat the machine and win !!!!")

start()
screen.exitonclick()
