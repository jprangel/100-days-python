from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if snake.snake_head.distance(food) < 18:
        food.refresh()
        scoreboard.score_point()
        snake.extend()
        
    # Detect collision with the limit of the screen (wall)
    snake_xcor = snake.snake_head.xcor()
    sneake_ycor = snake.snake_head.ycor()
    
    if snake_xcor > 280 or snake_xcor < -300 or sneake_ycor > 300 or sneake_ycor < -290:
        is_game_on = False
        scoreboard.game_over()
        
    # Detect collision with snake tail  
    for s in snake.snake_obj[1:]:
        if snake.snake_head.distance(s) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()

