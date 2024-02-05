from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen
import time

#screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#paddles
player_one = Paddle(x=350, y=0)
player_two = Paddle(x=-350, y=0)

#contol
screen.listen()
screen.onkey(fun=player_one.up, key="Up")
screen.onkey(fun=player_one.down, key="Down")
screen.onkey(fun=player_two.up, key="w")
screen.onkey(fun=player_two.down, key="s")

#ball
ball = Ball()

#scoreboard
scoreboard = Scoreboard()

#game is on untill one player reaches 10
# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with the player's paddle
    if ball.distance(player_one) < 60 and ball.xcor() >= 330:
        ball.bounce_x()

    # Detecting collision with the opponent's paddle
    if ball.distance(player_two) < 60 and ball.xcor() <= -330:
        ball.bounce_x()

    # Detecting collision with the bound
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.increase_player_two_score()
    elif ball.xcor() < -380:
        ball.refresh()
        scoreboard.increase_player_one_score()

    # Check when to end
    player_one_score = scoreboard.player
    player_two_score = scoreboard.opponent

    if player_one_score == 10 or player_two_score == 10:
        game_is_on = False

#display final winner
scoreboard.compare_score()

# Exit when it completes
screen.exitonclick()
