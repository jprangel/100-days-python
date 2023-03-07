from flask import Flask, render_template

app = Flask(__name__)

web_page = "index.html"

@app.route("/")
def home():
    return render_template(web_page)

if __name__ == "__main__":
    app.run(debug=True)