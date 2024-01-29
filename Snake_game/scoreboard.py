from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 275)

    def display_score(self, score):
        self.write(arg=f"Score: {score}", move=False, align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", move=False, align=ALIGNMENT, font=FONT)
    