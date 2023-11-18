from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<int:x>/<int:y>/<color>/<color_1>')     
def index(x,y,color,color_1):
    return render_template("index.html", x=x , y=y, color=color, color_1=color_1)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5003)   
