from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        #coordinates
        self.x = x
        self.y = y
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5, outline=1)
        self.penup()
        self.setposition(x, y)
        self.showturtle()

    def up(self):
        self.y += 40
        self.goto(self.x, self.y)
        
    def down(self):
        self.y -= 40
        self.goto(self.x, self.y)
