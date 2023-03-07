from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    global magic_number
    magic_number = random.choice(range(3,10))
    return "<h1> Guess a number between 0 and 9 </h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<number>")
def guess_number(number):
    number = int(number)
    if number < magic_number:
        return "<h1 style='color:red;'> Too low, try again ! </h1>" \
            "<img src='https://media.giphy.com/media/WZAUKr4TBRDxu/giphy.gif'>"
                
    elif number > magic_number:
        return "<h1 style='color:purple;'> Too high, try again ! </h1>" \
            "<img src='https://media.giphy.com/media/19x5KTWn0Vfmo/giphy.gif'>"
                
    elif number == magic_number:
        return "<h1 style='color:green;'> You found me !! </h1>" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
        
if __name__ == "__main__":
    app.run(debug=True)