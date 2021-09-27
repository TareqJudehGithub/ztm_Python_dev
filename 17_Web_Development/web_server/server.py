
from flask import Flask, render_template, url_for
from markupsafe import escape

# instantiate app from class Flask
app = Flask(__name__)
print(__name__)

# homepage
@app.route("/")
def main_page():
  return render_template(escape("./html/index.html"))

# blog
@app.route("/blog")
def blog():
  return escape("<h1>Welcome to the blog!</h1>")

# dogs blog
@app.route("/about")
def dogs_blog():
  return render_template(escape("./html/about.html"))


# users
@app.route("/users/<username>/<int:userid>")
def greet_users(username=None, userid=None):
  return render_template(escape("./html/index.html"), user=username, id=userid)

if __name__ == "__main__":
  app.run()




