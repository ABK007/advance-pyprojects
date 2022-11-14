from turtle import Screen, Turtle
import random

john = Turtle()
my_screen = Screen()

is_race_on = False # for controlling while loop

my_screen.setup(width=500, height=400) # defining screen size

user_bet = my_screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ") # popup window for user input

turtle_color = ["green","black","blue","yellow","orange","red"] # turtle color list

x_cordinate = -230 # coordinate of x axis
y_coordinate = -50 # coordinate of y axis

turtle_list = [] # list of turtle objects

for turtle_index in range(6):
    # creating turtle object with color and coordinates defined
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.goto(x = x_cordinate, y = y_coordinate)
    y_coordinate += 25
    turtle_list.append(new_turtle)
    
if user_bet: # checking if user has entered the input
    is_race_on = True
    
while is_race_on: # if user has entered input, the while loop will start running
    
    for turtle in turtle_list:
        # turtle is moving forward
        if turtle.xcor() > 230: 
            # if a turtle reaches greater than 230 in x axis
            is_race_on = False
            winner_turtle_color = turtle.pencolor()
            if winner_turtle_color == user_bet:
                print(f"You have won!, the {winner_turtle_color} turtle is the winner")
            else:
                print(f"You have lost!, the {winner_turtle_color} turtle is the winner")
        
        distance_to_cover = random.randint(0, 10)
        turtle.forward(distance_to_cover)
        
        


my_screen.exitonclick() # Screen will close on a click