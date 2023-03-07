from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_text_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_page = "blog.html"
home_blog_page = "home_blog.html"

def conn(url: str, param: str):
    r = requests.get(url, params=param)
    website_content = r.json()
    r.raise_for_status()
    return website_content

@app.route("/")
def home():
    return render_template(home_blog_page)

@app.route("/blog")
def get_blog():
    all_post = conn(blog_text_url, param=None)
    return render_template(blog_page, posts=all_post)
    
if __name__ == "__main__":
    app.run(debug=True)