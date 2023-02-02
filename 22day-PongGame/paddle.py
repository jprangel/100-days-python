from turtle import Turtle

WIDTH = 5
LENGHT = 1
OUTLINE = 1
COLOR = "white"
SHAPE = "square"
DISTANCE = 20

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.paddle_wid = WIDTH
        self.paddle_len = LENGHT
        self.paddle_out = OUTLINE
        self.paddle_pos = position
        self.create_paddle()
        
    def create_paddle(self):
        self.penup()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(self.paddle_wid, self.paddle_len, self.paddle_out)
        self.goto(self.paddle_pos)
        
    def up(self):
        """ Move the paddle Up"""
        y = self.ycor() + DISTANCE
        self.goto(self.xcor(), y)

    def down(self):
        """ Move the paddle Down"""
        y = self.ycor() - DISTANCE
        self.goto(self.xcor(), y)
        
        


        