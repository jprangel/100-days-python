from flask import Flask, render_template
import requests

app = Flask(__name__)

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

def conn(url: str, param: str):
    r = requests.get(url, params=param)
    website_content = r.json()
    r.raise_for_status()
    return website_content

@app.route('/')
def home():
    global all_posts
    all_posts = conn(BLOG_URL, param=None)
    return render_template("index.html", posts = all_posts)

@app.route("/post/<blog_id>")
def get_post(blog_id):
    return render_template("post.html", posts = all_posts, page = int(blog_id))

if __name__ == "__main__":
    app.run(debug=True)
