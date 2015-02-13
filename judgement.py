from flask import Flask, render_template, redirect, request
import model
q = model.session.query

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return render_template("welcome.html")

@app.route("/userlist")
def view_all_users():
    user_list = q(model.User).all()
    return render_template("userlist.html", user_list=user_list)

@app.route("/signup", methods=["POST", "GET"])
def signup():

    email = request.form.get ("email")
    password = request.form.get ("password")
    zipcode = request.form.get ("zipcode")
    age = request.form.get ("age")

    existent_email = q(model.User).filter(model.User.email == email).first()
    
    if existent_email == None:
        new_user=model.User(email=email, password=password, zipcode=zipcode, age=age)
        model.session.add(new_user)
        model.session.commit()
        return render_template("login.html", email=email, password=password, zipcode=zipcode, age=age, message="Welcome, ")



    else:
        return render_template("ERROR.html")



   
@app.route("/login", methods=["POST", "GET"])
def login():
    

    em = request.form.get("em")
    pw = request.form.get("pw")

    user_check = q(model.User).filter(model.User.email == em, model.User.password == pw).first()

    if user_check != None:
        return render_template("login.html", email = em, message="Thanks for logging in, ")
  
    else:
        return render_template("ERROR.html")


@app.route("/directme", methods=["POST", "GET"])
def gohere():
    where = request.form.get("action_dropdown")

    if where == "rate_movies":
        return render_template("ratemovies.html")
    
    elif where == "view_ratings":
        return render_template("viewratings.html")

    elif where == "recommend":
        return render_template("getrec.html")
    
    else:
        return view_all_users()

@app.route("/userratings/<int:id>")
def show_user_ratings(id):
    user_ratings_info = q(model.Rating).filter(model.Rating.user_id == id).all()
    movies_info = q(model.Movie).all()
    list_1 = []
    for rating in user_ratings_info:
        if rating.movie_id == :
            list_1 = list_1.append([movies_info.name, rating.rating])
#START HERE ON FRIDAY

    return render_template("user_ratings.html", user_ratings_info=list_1)

if __name__ == "__main__":
    app.run(debug = True)