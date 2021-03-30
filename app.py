from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash

from lib import database

print(generate_password_hash("Atto2525!"))

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/signup")
def signup() -> str:
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def post_signup() -> str:
    print(request.form.get("password"))
    print(request.form.get("username"))
    # with database.cursor as cursor:
    #     sql = "INSERT INTO light_blog.users (name,password) VALUES ($2,$3)"
    #     cursor.execute(sql,)
    return render_template("success-signup.html")


app.run()
