import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
states_list = df["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    title = str(len(guessed_states)) + '/50 States Correct' if len(guessed_states) > 0 else "Guess the State"
    answer = screen.textinput(title=title, prompt="What's another state name?").title()

    if answer == 'Exit':
        missing_states = [state for state in states_list if state not in guessed_states]
        missing_states_data = pd.DataFrame(missing_states)
        missing_states_data.to_csv("states_to_learn.csv")
        break
    elif answer in states_list:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = df[df.state == answer]
        t.goto(int(state.x), int(state.y))
        t.write(answer)
