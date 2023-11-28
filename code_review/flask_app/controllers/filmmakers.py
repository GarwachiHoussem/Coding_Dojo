from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.filmmaker_model import Filmmaker

@app.route('/')
def index():
    return redirect('/filmmakers')


@app.route('/filmmakers')
def filmmakers():
    all_filmmakers = Filmmaker.get_all()
    return render_template('filmmakers.html',all_filmmakers=all_filmmakers)

@app.route('/create/filmmaker', method=['POST'])
def create_filmmakers():
    data = {
        "name": request.form['name']
        
    }
    Filmmaker.save(data)
    return redirect('/filmmakers')


@app.route('/filmmaker/<int:id>')
def show_filmmakers(id):
    data= {"id":id}
    filmaker=Filmmaker.get_by_id(data)
    return render_template('show_filmmaker=filmmaker')



