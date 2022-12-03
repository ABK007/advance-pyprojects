import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



cars_speed = 0.1
STARTING_POSITION = (0, -280)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# creating turtle
turtle = Player()


# generating random cars
car_manager = CarManager()


# creating scoreboard
scoreboard = Scoreboard()

# player controls
screen.listen()
screen.onkey(turtle.go_up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(cars_speed)
    screen.update()
    
    # ganerating and moving cars
    car_manager.create_car()
    car_manager.move_car() 
    
    # detecting collision with the car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False
            
    # detect the turtle crossed the road
    if turtle.ycor() > 260:
        cars_speed *= 0.7
        turtle.goto(STARTING_POSITION)
        scoreboard.next_level()
        
            
    







screen.exitonclick()