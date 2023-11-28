from flask_app import app

#! All contollers must be imported HERE
# from flask_app.controllers import users


if __name__ == "__main__":
    app.run(debug=True, Port=5001)
