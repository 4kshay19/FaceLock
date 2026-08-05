import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/profile")
def profile():
    user = {
        "name": "Arjun Reddy",
        "email": "arjun.reddy@example.com",
        "joined": "July 2026",
        "face": "Registered",
        "encrypted": 18,
        "decrypted": 11
    }
    return render_template("profile.html", user=user)
from flask import Flask, render_template, request, redirect, url_for, session
import os
import json

app = Flask(__name__)
app.secret_key = "facelock_secret_key"
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "Passwords do not match"

        session["username"] = username

        user = {
            "username": username,
            "fullname": fullname,
            "email": email,
            "password": password
        }

        file_path = "users/users.json"

        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                users = json.load(f)
        else:
            users = []

        users.append(user)

        with open(file_path, "w") as f:
            json.dump(users, f, indent=4)

        return redirect(url_for("register_face"))

    return render_template("register.html")
from werkzeug.security import generate_password_hash

hashed_password = generate_password_hash(password)

user = {
    "username": username,
    "fullname": fullname,
    "email": email,
    "password": hashed_password
}