from flask_app import app

from flask_app.controllers import users

@app.route('/user/<username>')
def user_profile(username):
    return f'Profile page of {username}'


if __name__ == '__main__':
    app.run(debug=True, port=5002) 