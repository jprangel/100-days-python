from turtle import Turtle

START_POS = (0, -280)
MOVE_DIST = 10
FINAL_POS_Y = 280
HEAD = 90
COLOR = "white"
SHAPE = "turtle"

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.penup()
        self.goto(START_POS)
        self.setheading(HEAD)
        
    def up(self):
        """ Move turtle to Up"""
        self.forward(MOVE_DIST)
        
    def end(self):
        """ Reset turtle position"""
        self.goto(START_POS)
        self.setheading(HEAD)
        