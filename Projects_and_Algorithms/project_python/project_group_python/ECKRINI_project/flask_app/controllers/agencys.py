from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.car import Car
from flask_app.models.agency import Agency
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/agencys/create", methods=["POST"])
def signup_agency():
    print(request.form)

    if Agency.validate(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data = {**request.form, "password": pw_hash}

        agency_id = Agency.create(data)
        session["agency_id"] = agency_id
        return redirect("/")

    return redirect("/signup")

@app.route('/signup_agency')
def signup2():
    return render_template("signup_agency.html")


# ___________________LOGIN_________________________
@app.route("/login_agency", methods=["POST"])
def login_agency():
    agency = Agency.get_by_email({"email": request.form["email"]})
    if not agency:
        flash("Invalid Email / Password", "login")
        return redirect("/login")
    if not bcrypt.check_password_hash(agency.password, request.form["password"]):
        flash("Invalid Email / Password", "login")
        return redirect("/login")
    session["user_id"] = agency.id
    return redirect("/")

@app.route('/login_agency')
def login2():
    return render_template("login_agency.html")

@app.route('/dashboard_agency')
def dashboard_agency():
    
    results = Car.get_all_cars()
    print(results)
    userconnect=User.get_by_id({'id':session['user_id']})
    return render_template("dashboard_agency.html" , results=results,  userconnect=userconnect)
