from turtle import Screen, Turtle

john = Turtle()
my_screen = Screen()

john.shape("turtle") # changes the shape of the turtle
john.color("green") # changing the color of the turtle

my_screen.listen() # keep notes if the button is pressed or not


def move_forward():
    """moves turtles forward 10 steps"""
    john.forward(10)
    
def move_backward():
    """moves turtles backward 10 steps"""
    john.backward(10)
    
def turn_right():
    """orient turtle right 10 degrees"""
    john.right(10)
    
def turn_left():
    """orient turtle left 10 degrees"""
    john.left(10)
    
def clear_drawing():
    """clears the drawing and retuns the turtle to starting point"""    
    john.setpos(0.00,0.00)
    john.clear()
    
    
    
my_screen.onkeypress(fun =move_forward, key="w") # moves forward when w is pressed
my_screen.onkeypress(fun =move_backward, key="s") # moves backward when s is pressed
my_screen.onkeypress(fun =turn_left, key="a") # orients left when a is pressed
my_screen.onkeypress(fun =turn_right, key="d") # orients right when d is pressed
my_screen.onkeypress(fun =clear_drawing, key="c") # clears and returns home when c is pressed





my_screen.exitonclick() # Screen will close on a click