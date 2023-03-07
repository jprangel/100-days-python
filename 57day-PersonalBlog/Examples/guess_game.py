from flask import Flask, render_template
import requests

app = Flask(__name__)

web_page = "index.html"
agefy_url = "https://api.agify.io/"
genderize_url = "https://api.genderize.io/"

def conn(url: str, param: str):
    r = requests.get(url, params=param)
    website_content = r.json()
    r.raise_for_status()
    return website_content

def guess_age(d):
    data = conn(url = agefy_url, param=d)
    return data['age']

def guess_gender(d):
    data = conn(url = genderize_url, param=d)
    return data['gender']

@app.route("/")
def home():
    return render_template(web_page)

@app.route("/guess/<input_name>")
def guess_name(input_name):
    if input_name not in vars():
        input_name = "test"
    d = { 'name': input_name }
    api_age = guess_age(d)
    api_gender = guess_gender(d)
    return render_template(guess_page, user = input_name, age = api_age, gender = api_gender)
    
if __name__ == "__main__":
    app.run(debug=True)