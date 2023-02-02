# Pong game
# TODO - Score on top, who reach 10 first win
# TODO - 2 players control diff decks, one each side - 1 player (arrows) 2 player (w and s keys), the decks does only up and down on their sides.
# TODO - if the ball hits opponent wall, the play score one point and the ball is release to the opponent side from the middle.
# TODO - if the ball hits the up/down wall the ball goes in 15 degress forward.
# TODO - if the player hits the ball with their deck, the ball goes in the opposite direction


# 800 witdh / 400 / max 375 = x
# 600 heigh / 300 / max: 275 = y

from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


is_game_on = True
while is_game_on:
    score.draw_middle_line()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with top and down walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with right_paddle
    ball_dist_r_paddle = ball.distance(right_paddle)
    ball_dist_l_paddle = ball.distance(left_paddle)
    if (ball_dist_r_paddle < 60 and ball.xcor() > 335) or (ball_dist_l_paddle < 60 and ball.xcor() < -335):
        ball.bounce_x()
        
    # Detect score point
    if ball.xcor() >= 390:
        score.score_left_point()
        ball.reset_pos()
        time.sleep(0.3)
    
    if ball.xcor() <= -392:
        score.score_right_point()
        ball.reset_pos()
        time.sleep(0.3)

    # Detect the winner
    if score.score_left == 10:
        score.win_msg("left")
        is_game_on = False
        
    elif score.score_right == 10:
        score.win_msg("right")
        is_game_on = False
        
screen.exitonclick()
