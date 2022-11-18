from turtle import Turtle

X_COR = -20
Y_COR = 260

class Scoreboard(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.color("black")
        self.pencolor("white")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.score = 0
        self.goto(X_COR, Y_COR)
        self.hideturtle()
        
        
        
    def write(self):
        super().clear()
        super().pendown()
        super().write(f"Score: {self.score}", move=False, align='left', font=('Arial', 15, 'normal'))
        super().penup()
        
    def add_score(self):
        self.score += 1
        
    def game_over(self):
        self.goto( -110, 0)
        super().write("GAME OVER", move=False, align='left', font=('Arial', 25, 'normal'))
        