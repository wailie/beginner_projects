from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player = 0
        self.opponent = 0
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(200, 200)
        self.write(arg=f"{self.player}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(-200, 200)
        self.write(arg=f"{self.opponent}", move=False, align=ALIGNMENT, font=FONT)

    def increase_player_one_score(self):
        self.player += 1
        self.display_score()

    def increase_player_two_score(self):
        self.opponent += 1
        self.display_score()

    def compare_score(self):
        self.goto(0, 50)
        winner = ""
        if self.player > self.opponent:
            winner += "Player 2(right) win!"
        elif self.opponent > self.player:
            winner += "Player 1(left) win!"
        self.write(arg=winner, move=False, align=ALIGNMENT, font=("Courier", 20, "bold"))
        