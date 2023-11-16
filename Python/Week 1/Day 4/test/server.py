from flask import Flask 
app = Flask(__name__)

#http:127.0.0.1/
@app.route('/')
def hello_world():
    return 'Hello World!'

#http:127.0.0.1/hello
@app.route('/Hello')
def hello():
    return "Hello From Server"

#http:127.0.0.1/hello/user
@app.route('/hello/<user>')
def say_hello():
    return f"<h1> Hello {int:user} james <h1>"
#http:127.0.0.1/user/<username>/<age>
@app.route('/user/<username>/<int:age>')
def user_info(username,age):
    return f"<h1>USERNAME : {username} br/Age: {age}"

#http:127.0.0.1/index
@app.route('/index')
def index ():
    return render_template("index.html")




if __name__=="__main__":
    app.run(debug=True, port=1337)

