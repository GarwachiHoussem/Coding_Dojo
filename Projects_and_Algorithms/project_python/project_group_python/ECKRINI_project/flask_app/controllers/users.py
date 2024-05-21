from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.car import Car
from flask_app.models.agency import Agency
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

 

@app.route('/')
def index():
    if "user_id" in session:
        userconnect=User.get_by_id({'id':session['user_id']})
    else:
        userconnect=""
    return render_template('index.html',userconnect=userconnect)

# ___________________SIGNUP_______________________
@app.route("/users/create", methods=["POST"])
def signup():
    print(request.form)
    if User.validate(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data = {**request.form, "password": pw_hash}

        user_id = User.create(data)
        session["user_id"] = user_id
        return redirect("/")

    return redirect("/signup")




@app.route('/signup')
def signup1():
    return render_template("signup.html")

# ___________________LOGIN_________________________
@app.route("/login", methods=["POST"])
def login():
    user = User.get_by_email({"email": request.form["email"]})
    if not user:
        flash("Invalid Email / Password", "login")
        return redirect("/login")
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid Email / Password", "login")
        return redirect("/login")
    session["user_id"] = user.id
    if user.role=="client":
        return redirect("/dashboard_client")
    else:
        return redirect("/dashboard_agency")



@app.route('/login')
def login1():
    return render_template("login.html")

@app.route('/contact')
def contact():
    userconnect = ''
    return render_template("contact.html",userconnect=userconnect)

@app.route('/booking')
def booking1():
    userconnect = ''
    return render_template("booking.html",userconnect=userconnect)

@app.route('/booking/<car_id>/<agency_id>' , methods=['GET'])
def booking(car_id, agency_id):
    # car_id = request.args.get('car_id')
    # agency_id = request.args.get('agency_id')
    # print(car_id)
    userconnect =  ''
    return render_template("booking.html", car_id=car_id, agency_id=agency_id, userconnect=userconnect)

@app.route('/dashboard_client')
def dashboard_client():
    user_id =  session["user_id"]
    results = Car.get_user_rented_cars({"user_id": user_id})
    print(results)
    userconnect=User.get_by_id({'id':session['user_id']})
    return render_template("dashboard_client.html" , results=results,  userconnect=userconnect)

# @app.route('/dashboard_agency')
# def dashboard_agency():
#     userconnect=User.get_by_id({'id':session['user_id']})
#     return render_template("dashboard_agency.html",  userconnect=userconnect)


@app.route('/agency_cars')
def agency_cars():
    userconnect = ''
    return render_template("agency_cars.html" , userconnect=userconnect)


@app.route('/new/car')
def new_car():
    userconnect = ''
    return render_template("add_car.html" , userconnect=userconnect)




# ___________________LOGOUT_________________________
@app.route('/logout', methods =['POST'])
def logout():
    session.clear()
    return redirect('/')