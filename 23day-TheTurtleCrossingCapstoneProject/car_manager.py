from turtle import Turtle
import random
import time

COLOR = ["blue", "green", "purple", "magenta", "yellow", "orange", "gray", "red", "brown", "peru", "pink", "lime"]
START_MOVE_DIST = 5
INCREMENT_MOVE_DIST = 10
CARS_OBJ = []
START_CAR_POS_X = 297
SECOND_CAR_POS = 20
CAR_POS_Y = [-240, -120, -180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180, 210, 240]
SHAPE = "square"

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_obj = CARS_OBJ
        self.create(0)
        
    def create(self, level):
        """ Create cars in the screen in the initial postion"""
        x = self.get_level(level)
        for c in range(x):
            obj1 = Turtle()
            obj2 = Turtle()
            cars = (obj1, obj2)
            self.set_car(obj1, obj2)
            y = random.choice(CAR_POS_Y)
            cars[0].goto(START_CAR_POS_X, y)
            x = START_CAR_POS_X + SECOND_CAR_POS
            cars[1].goto(x,y)
            CARS_OBJ.append(cars)
    
    def set_car(self, obj1, obj2):
        """ Set characterist to the cars"""
        color = random.choice(COLOR)
        for c in obj1, obj2:
            c.penup()
            c.shape(SHAPE)
            c.color(color)
        
    def get_level(self, level):
        """ Check user level to increase number of cars"""
        if level < 3: # Easy
            return random.randint(3, 5)
        elif level > 3 and level < 6: # Medium
            return random.randint(5, 8)
        else: # Hard
            return random.randint(8, 12)
        
    def move(self, level):
        """ Move the car based on the user level"""
        speed = 5 + (2 * level)
        for c in range(len(CARS_OBJ)):
            c = random.choice(CARS_OBJ)
            for i in range(2):
                c[i].backward(speed)
            
    def reset(self):
        """ Create a new set of car in the initial position"""
        CARS_OBJ.clear()
        self.create()