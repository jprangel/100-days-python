from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_SHAPE = "square"
SNAKE_FILL = "green"
SNAKE_PEN = "green yellow"
SNAKE_PEN_SIZE = 5

class Snake:


    def __init__(self):
        self.snake_obj = []
        self.snake_create()
        self.snake_head = self.snake_obj[0]


    def snake_create(self):
        """"" Create snake boby with 3 segments in 3 postion in sequence """
        for p in START_POS:
            self.add_segment(p)
                           

    def move(self):
        """" Moving snake from the tail to head in order to the body follow the head """
        for p in range(len(self.snake_obj)-1, 0, -1):
            x = self.snake_obj[p - 1].xcor()
            y = self.snake_obj[p - 1].ycor()
            self.snake_obj[p].goto(x, y)
        self.snake_head.forward(MOVE_DIST)
        
    
    def up(self):
        """ Turn the head of snake to go Up and disable backwards"""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    
    
    def down(self):
        """ Turn the head of snake to go Down and disable snake goes backwards"""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    
        
    def left(self):
        """ Turn the head of snake to go Left and disable snake goes backwards"""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    
        
    def right(self):
        """ Turn the head of snake to go Right and disable snake goes backwards"""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
            
            
    def add_segment(self, postion):
        """ Add a segment in the snake body"""
        snake = Turtle(shape=SNAKE_SHAPE)
        snake.pensize(SNAKE_PEN_SIZE)
        snake.pencolor(SNAKE_PEN)
        snake.fillcolor(SNAKE_FILL)
        snake.penup()
        snake.goto(postion)
        self.snake_obj.append(snake)
        
        
    def extend(self):
        """ Extend the snake body in 1 segment at the end of the body"""
        self.add_segment(self.snake_obj[-1].position())
        