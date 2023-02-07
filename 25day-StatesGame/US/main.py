import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
states_csv = pandas.read_csv("50_states.csv")
all_states = states_csv.state.to_list()
guessed_states = []
total_states = 50

while len(guessed_states) < total_states:
    guess_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                   prompt="What's another state's name?").title()
    if guess_state in all_states:
        guessed_states.append(guess_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = states_csv[states_csv.state == guess_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        
    if guess_state == "Exit":
        missing_states = [s for s in all_states if s not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("state_to_learn.csv")
        break
