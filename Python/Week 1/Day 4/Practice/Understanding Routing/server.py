from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)

# Create a new instance of the Flask class called "app"
@app.route('/')     
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')        
def Dojo():
    return 'Dojo'

@app.route('/say/flask')        
def HI_flask():
    return 'Hi Flask'

@app.route('/say/michael')        
def hi_michael():
    return 'Hi michel'

@app.route('/say/john')        
def hi_jhon():
    return 'Hi john'

@app.route('/repeat/<times>/<name>')        
def hello (times,name):
    return f"<h1>{name}<h1>"* int (times)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5000)   
