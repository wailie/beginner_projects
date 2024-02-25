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
states = data.state.to_list()
correct_states = []
missing_states = states

while len(correct_states) != 50:
    answer = screen.textinput(title=f"{len(correct_states)}/50 States", prompt="What's the state's name?").title()
    if answer == "Exit":
        break
    if check_answer(states, answer):
        correct_states.append(answer)
        #getting answer row in dataframe
        correct_state = data[data.state == answer]
        write_state(answer, int(correct_state.x.iloc[0]), int(correct_state.y.iloc[0]))
        missing_states.remove(answer)


# states to learn.csv
# save the missing states to a .csv

missing_states_table = {
    "States you need to learn": missing_states
}
table_data = pandas.DataFrame(missing_states_table)
table_data.to_csv("missing_states.csv")

screen.exitonclick()

