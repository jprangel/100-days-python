import turtle
import pandas

screen = turtle.Screen()
screen.title("Romanian Counties Game")
screen.setup(width=800, height=800)
image = "romania.gif"

screen.addshape(image)
turtle.shape(image)

counties_csv = pandas.read_csv("romania.csv")
all_counties = counties_csv.county.to_list()
guessed_counties = []
total_counties = 41

while len(guessed_counties) < total_counties:
    guess_county = screen.textinput(title=f"{len(guessed_counties)}/{total_counties} Counties Correct", 
                                   prompt="What's another county name?").title()
    if guess_county in all_counties:
        guessed_counties.append(guess_county)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        county_data = counties_csv[counties_csv.county == guess_county]
        t.goto(int(county_data.x), int(county_data.y))
        t.write(county_data.county.item(), font=("Arial", 12, "bold"))
        
    if guess_county == "Exit":
        missing_counties = [c for c in all_counties if c not in guessed_counties]
        df = pandas.DataFrame(missing_counties)
        df.to_csv("counties_to_learn.csv")
        break

