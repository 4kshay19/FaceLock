from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register_face.html")

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
        "name": " ",
        "email": "mike@example.com",
        "joined": "July 2026",
        "face": "Registered",
        "encrypted": 18,
        "decrypted": 11
    }
    return render_template("profile.html", user=user)   