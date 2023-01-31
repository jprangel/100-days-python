from turtle import Turtle
import random

FOOD_SPEED = "fastest"
FOOD_SHAPE = "turtle"
XL_EDGE = -250
XR_EDGE = 250
YU_EDGE = 250
YD_EDGE = -250


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.colors = ["pink", "blue", "magenta", "yellow", "orange", "purple", "peru", "red", "gray"]
        self.shape(FOOD_SHAPE)
        self.color(self.random_color())
        self.speed(FOOD_SPEED)
        self.penup()
        self.refresh()
        
    def random_color(self):
        """ Get a random color for the food"""
        return random.choice(self.colors)
    
    def refresh(self):
        """ Show the food in a random position"""
        rand_x = random.randint(XL_EDGE, XR_EDGE)
        rand_y = random.randint(YD_EDGE, YU_EDGE)
        self.color(self.random_color())
        self.goto(rand_x, rand_y)
        