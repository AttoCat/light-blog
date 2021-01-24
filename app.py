from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root() -> str:
    return render_template("index.html")


@app.route("/signup")
def signup() -> str:
    return render_template("signup.html")


app.run()
