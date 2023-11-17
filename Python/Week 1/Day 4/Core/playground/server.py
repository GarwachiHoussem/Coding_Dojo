from flask import Flask, render_template
app= Flask(__name__)

@app.route('/<int:x>/<color>')
def block(x,color):
    return render_template("index.html" , x=x, color=color)

@app.route('/')
def index():
    return 'hello'

if __name__=="__main__":   
    app.run(debug=True, port=5000)