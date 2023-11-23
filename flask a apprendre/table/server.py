from flask import Flask  
app = Flask(__name__)  

# @app.route('/author/<author>/<int:age>/<city/<int:code_zip>')
# def all_info(author,age,city,code_zip):
#     return f"<h2>{author} </br>{age} </br>{city} </br>{code_zip}</h2>"

@app.route('/author/<author>/<int:age>/<city>/<int:code_zip>')
def all_info(author, age, city, code_zip):
    return f"<h2>{author}</br> Age: {age} </br> City: {city} </br> Code: {code_zip}</h2>"

@app.route('/author/<author>/<int:age>')
def author_info(author, age):
    return f"<h1>Author:{author} </br> Age:{age}</h1>" 


@app.route('/author/<author>/<int:times>')
def author_name_times(author, times):
    return f"<h1>{author}</h1>" * times


@app.route('/author/<author>')
def author_name(author):
    return f"<h1>{author}</h1>"


@app.route('/user/<username>')          
def user_name_auto(username):
    return f"<h1>{username}</h1>"



@app.route('/name/1')          
def Ahmed():
    return "<h1>ahmed</h1>"

@app.route('/name')          
def Houssem():
    return 'Houssem'  

@app.route('/')          
def hello_world():
    return 'Hello World!'  


if __name__=="__main__":       
    app.run(debug=True, port=5001)  

