from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
import time


# screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game🐍")
screen.tracer(0)

# snake body
snake = Snake()

# food
food = Food()

#score
score = 0

#scoreboard
scoreboard = Scoreboard()

# control Up/Down/Left/Right keys
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.display_score(score)
    
    # detecting collision between food and snake
    if snake.head.distance(food.xcor(), food.ycor()) < 15:
        # clear the old score
        scoreboard.clear()
        # update the score
        score += 1
        scoreboard.display_score(score) 
        food.refresh()
        snake.extend()

    # detecting collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        scoreboard.game_over()
        is_game_on = False

    # detecting collision with snake's tail
    # if snake's head collides with any segment in the tail:
        #game over
    snake_bodies = snake.segments[1:-1]
    for snake_body in snake_bodies:
        if snake.head.distance(snake_body) < 10:
            scoreboard.game_over()
            is_game_on = False
































screen.exitonclick()