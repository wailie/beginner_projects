from turtle import Turtle
# constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
###

# coordinate set up
x = 0
y = 0

class Snake():
    def __init__(self):
        # coordinate set up
        x = 0
        y = 0
        self.segments = [] # all segments are individual turtles
        for _ in range(3):
            self.add_segment(x, y)
        self.head = self.segments[0] # first turtle or head


    def add_segment(self, x, y):
        snake_body = Turtle("square") 
        snake_body.penup()
        snake_body.color("white")
        snake_body.goto(x, y)
        x -= 20
        self.segments.append(snake_body)


    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())

    


    def move(self):
        """move each segment to next segment's position and move the head forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1): # 2 1 0
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(20)


    def up(self):
        """if the direction is not downward, change the snake heading to up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        """if the direction is not upward, change the snake heading to down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        """if the direction is not right, change the snake heading to left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        """if the direction is not left, change the snake heading to right"""
        if self.head.heading() != LEFT:   
            self.head.setheading(RIGHT)

