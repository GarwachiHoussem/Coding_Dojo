from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user import User
from flask_app.models.party import Party
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template("index.html")



@app.route('/dashboard')
def dashboard():
    if not "user_id" in session:
        return redirect("/")
    all_parties = Party.get_all()
    return render_template("dashboard.html", all_parties=all_parties)



@app.route('/register', methods=['post'])
def register():
    print("******", request.form, "---------------------")
    if User.validate(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {**request.form, "password" : pw_hash}
        user_id = User.create(data)
        session["user_id"] = user_id
        session["username"] = data["first_name"]
        return redirect("/dashboard")
    return redirect("/")


@app.route('/login', methods=['post'])
def login():
    user_from_db = User.get_by_email({'email': request.form["email"]})
    if not user_from_db:
        flash("Email doesn't exist. try to register first", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_from_db.password, request.form["password"]):
        flash("Password wrong please try again", "login")
        return redirect("/")
    session["user_id"] = user_from_db.id
    session["username"] = user_from_db.username
    return redirect("/")



@app.route("/login", methods=['post'])
def logout():
    session.clear()
    return redirect("/")