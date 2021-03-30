from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash

from lib import database

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/signup")
def signup() -> str:
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def post_signup() -> str:
    username = request.form.get("username")
    password = request.form.get("password")
    if (not username) or (not password):
        return render_template("signup.html", alert="ユーザーネーム又はパスワードが入力されていません")
    with database.cursor as cursor:
        sql = "INSERT INTO light_blog.users (name,password) VALUES (%s,%s)"
        cursor.execute(sql, (username, generate_password_hash(password)))
        database.connection.commit()
        return render_template("success-signup.html")


app.run()
