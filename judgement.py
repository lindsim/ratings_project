from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def dummy():
    return render_template("welcome.html")

@app.route("/userlist")
def view_all_users():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")




if __name__ == "__main__":
    app.run(debug = True)