from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("black")
        self.level = 1
        self.goto(x=-270, y=270)
        self.write(f"Level: {self.level}", move=False, align='left', font=('Arial', 15, 'normal'))
        
        
        
        

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", move=False, align='left', font=('Arial', 15, 'normal'))
        
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", move=False, align='center', font=('Arial', 15, 'normal'))
        

        
        
        
        
