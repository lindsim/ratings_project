from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def dummy():
    return render_template("welcome.html")

@app.route("/userlist")
def view_all_users():
    user_list = model.session.query(model.User).all()
    return user_list

@app.route("/ratings")
def user_ratings():
    pass

@app.route("/signupdone", methods=["GET", "POST"])
def signup():
    signup_process = {"GET": request.args.get, "POST": request.args.get}
    email = signup_process [request.method] ("email")
    password = signup_process [request.method] ("password")
    zipcode = signup_process [request.method] ("zipcode")
    age = signup_process [request.method] ("age")

    return render_template("signupdone.html", email=email, password=password, zipcode=zipcode, age=age)

@app.route("/signup", methods=["POST"])
def make_signup():

    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")




if __name__ == "__main__":
    app.run(debug = True)