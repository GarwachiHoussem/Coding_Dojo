from flask_app import app

#! All contollers must be imported HERE
from flask_app.controllers import users, parties


if __name__ == "__main__":
    app.run(debug=True)
