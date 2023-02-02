from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 80, 'bold')
GAME_OVER_FONT = ('Courier', 30, 'bold')
SCORE_COLOR = "white"
SCORE_L_POS = (-100, 200)
SCORE_R_POS = (100, 200)

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """ Show score board on the top of the screen"""
        self.clear()
        self.goto(SCORE_L_POS)
        self.write(f"{self.score_left}", align=ALIGN, font=FONT)
        self.goto(SCORE_R_POS)
        self.write(f"{self.score_right}", align=ALIGN, font=FONT)
        
    def score_left_point(self):
        """ Increase the points for left paddle"""
        self.score_left += 1
        self.update_scoreboard()
    
    def score_right_point(self):
        """ Increase the points for right paddle"""
        self.score_right += 1
        self.update_scoreboard()
        
    def win_msg(self, side):
        """ Show Game Over message to the user in the middle of the screen"""            
        self.home()
        self.write(f"!! The Winner is the {side} paddle !!", align=ALIGN, font=GAME_OVER_FONT)
        
    def draw_middle_line(self):
        self.penup()
        self.goto(0,300)
        self.setheading(270)
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)