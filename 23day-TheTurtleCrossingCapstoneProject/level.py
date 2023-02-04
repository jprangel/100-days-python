from turtle import Turtle

FONT = ('Courier', 24, 'bold')
GAME_OVER_FONT = ('Courier', 30, 'bold')
LEVEL_POS = (-230, 270)
ALIGN = "center"
START_END_LINE = [(-300, -260), (-300, 260)]
COLOR = "whiite"

class Level(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.level = 0
        self.start_end_line = START_END_LINE
        self.penup()
        self.hideturtle()
        self.get()
        
    def draw_lines(self):
        """ Draw start and end lines"""
        self.hideturtle()
        self.penup()
        self.color("white")
        for l in self.start_end_line:
            self.goto(l)
            for _ in range(30):
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)
        
    def get(self):
        """ Show level in the screen"""
        self.clear()
        self.goto(LEVEL_POS)
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)
        self.draw_lines()
        
    def up(self):
        """ Increase the level"""
        self.level += 1
        
    def gameover(self):
        """ Show Game Over message to the user in the middle of the screen"""            
        self.home()
        self.write(f"!! Game Over !!", align=ALIGN, font=GAME_OVER_FONT)
    
        
    

