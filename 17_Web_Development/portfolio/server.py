from flask import Flask, app, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def homepage():
  return render_template(escape("index.html"))


if __name__ == "__main__":
  app.run()