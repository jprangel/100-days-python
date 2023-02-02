from turtle import Turtle

COLOR = "lime"
SHAPE = "circle"

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.09
        self.speed("fastest")

        
    def create_ball(self):
        self.penup()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize()
    
    
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
            
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.6
        
    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.09
