from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 20, 'bold')
GAME_OVER_FONT = ('Courier', 30, 'bold')
SCORE_COLOR = "white"
SCORE_POS = (0, 270)

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.goto(SCORE_POS)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """ Show score board on the top of the screen"""
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)  
        
    def score_point(self):
        """ Increase the points"""
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        """ Show Game Over message to the user in the middle of the screen"""            
        self.home()
        self.write(f"!! GAME OVER !!", align=ALIGN, font=GAME_OVER_FONT)
