from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.x = self.xcor() + self.x_move
        self.y = self.ycor() + self.y_move
        self.goto(self.x, self.y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_y()
