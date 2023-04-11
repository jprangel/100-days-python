from flask import Flask, render_template, request
import requests

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/d514088408e90ce9793a").json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)

if __name__ == "__main__":
    app.run(debug=True)
