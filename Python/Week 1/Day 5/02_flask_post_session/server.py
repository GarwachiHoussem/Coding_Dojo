from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key=

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("*"20, request.form,"*"*20)
    return redirect('/display')

@app.route('/display')
def process():
    return render_template('/display.html')

if __name__ == "__main__":
    app.run(debug=True)
