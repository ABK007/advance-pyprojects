from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


turtle_xcor = 0 # variable to save initial x coordinate of the turtle object
game_on = True # Control while loop

# application window setup
my_screen = Screen()
my_screen.setup(width=600, height= 600)
my_screen.title("My snake game")
my_screen.bgcolor("black")
my_screen.tracer(0) # disables the animation
my_screen.listen()


snake = Snake() # creating snake object
food = Food() # creating food object
scoreboard = Scoreboard() # creating scoreboard object

    



while game_on:
    
    my_screen.update() # updates the screen when animation is off
    time.sleep(0.1) # adds delay to control speed of the turtle
    scoreboard.write() # adds score on top of the screen
    
    # controls the snake movement
    snake.move() # moves forward
    my_screen.onkey(fun=snake.up, key="Up") # moves up
    my_screen.onkey(fun=snake.down, key="Down") # moves down
    my_screen.onkey(fun=snake.left, key="Left") # moves left
    my_screen.onkey(fun=snake.right, key="Right") # moves right
    
    # detects the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend_snake ()
        
    # detects the collision with walls of screen
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.game_over()
        game_on = False
        
    # detects the collision with the tail
    for segment in snake.snake_segments[1: ]:
        if snake.head.distance(segment) < 10:
            game_on = False  
            scoreboard.game_over()
        
        
        





my_screen.exitonclick()