from flask import Flask, redirect, url_for
#redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the main page  <h1>HELLO</h1>"

@app.route("/temp")
def temp_page():
    return "This is a temp page. You went here without reason"

@app.route("/<name>")
def user(name):
    return f"<h1> Hello, {name} </h1>"

## to redirect in the case of an incorrect link. 
@app.route("/admin")
def admin():
    return redirect(url_for("temp_page"))




if __name__ == "__main__":
    app.run()