import pandas
import turtle

FONT = ("Roboto", 13, "normal")

def check_answer(states, ans):
    for state in states:
        if state == ans:
            return True
        
def write_state(state, x, y):
    state_writer = turtle.Turtle()
    state_writer.hideturtle()
    state_writer.penup()
    state_writer.goto(x, y)
    state_writer.write(arg=f"{state}", move=False, align="center", font=FONT)

#bg image
img = "blank_states_img.gif"

#screen
screen = turtle.Screen()
screen.setup(width=735, height=500)
screen.title("U.S. States Quiz")

#bg
screen.addshape(img)
turtle.shape(img)

#data
data = pandas.read_csv("50_states.csv")

#states
states = data.state
correct_states = []

while not len(correct_states) == 50:
    answer = screen.textinput(title=f"Guess the State {len(correct_states)}/50", prompt="What's the state's name?").title()
    if check_answer(states, answer):
        correct_states.append(answer)
        correct_state = data[data.state == answer]
        write_state(answer, int(correct_state.x.iloc[0]), int(correct_state.y.iloc[0]))

screen.exitonclick()