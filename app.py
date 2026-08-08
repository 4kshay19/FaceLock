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
username = request.form["username"]

folder_path = os.path.join("static", "faces", username)

os.makedirs(folder_path, exist_ok=True)
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

        # Save username in session
        session["username"] = username

        # Create user's face folder
        folder_path = os.path.join("static", "faces", username)
        os.makedirs(folder_path, exist_ok=True)

        return redirect(url_for("register_face"))

    return render_template("register.html")

@app.route("/register-face")
def register_face():

    username = session.get("username")

    return render_template(
        "register_face.html",
        username=username
    )
from flask import render_template
import os

UPLOAD_FOLDER = "uploads"

@app.route("/myfiles/<username>")
def my_files(username):

    user_folder = os.path.join(UPLOAD_FOLDER, username)

    files = []

    if os.path.exists(user_folder):
        for file in os.listdir(user_folder):
            path = os.path.join(user_folder, file)

            files.append({
                "name": file,
                "size": round(os.path.getsize(path) / 1024, 2)
            })

    return render_template(
        "my_files.html",
        username=username,
        files=files
    )
from encryption.encrypt import encrypt_file
import os
from flask import request, redirect, url_for, flash