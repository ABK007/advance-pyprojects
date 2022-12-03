from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0),(-40, 0)]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():

    
    def __init__(self):
        """initializing the constructors"""
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        
    def create_snake(self):
        """create snake instance with pre defined attributes"""
        for position in POSITIONS:
    # creating 3 instances of turtle object to make a snake
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup() # it will stop turtle to draw
        new_segment.goto(position)
        self.snake_segments.append(new_segment)
        
        
    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position())
        
    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
        
            
    def move(self):
        """Allows forward motion of the snake"""
        for seg_num in range(len(self.snake_segments)-1, 0, -1):
        # other segments follows the first segment by following its coordinates
            new_x = self.snake_segments[seg_num - 1].xcor() # fetching x coordinate of the first segment 
            new_y = self.snake_segments[seg_num - 1].ycor() # fetching y coordinates of the first segment
            self.snake_segments[seg_num].goto(new_x, new_y) # setting the coordinates of segments
        self.snake_segments[0].forward(MOVE_DISTANCE)
        
    
    def up(self):
        """snakes change direction to up"""
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)
        
    def down(self):
        """snakes change direction to down"""
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)
    
    def right(self):
        """snakes change direction to right"""
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)
        
    def left(self):
        """snakes change direction to left"""
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)
        
        