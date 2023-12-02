from flask import render_template, request, redirect, session, url_for
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def home():
    return redirect('/Users/new')

@app.route('/Users/new')
def new_User():
    if 'id' not in session:
        return redirect('/')
    return render_template("new_User.html")

@app.route('/Users/edit/<int:id>')
def edit_User(id):
    if 'id' not in session:
        return redirect('/')
    User = User.get_User_by_id({'id':id})
    return render_template("edit_User.html" ,User= User)

@app.route('/Users/update/<int:id>',methods = ['POST'])
def update_User(id):
    if User.validate(request.form):
        print(request.form)
        data = {
            **request.form,
            'id':id
        }
        print(data)
        User.update_User(data)
        return redirect('/dashboard')
    # return redirect('/Users/edit/<int:id>')
    return redirect(url_for('edit_User', id=id))

@app.route('/Users/create', methods=['POST'])
def create_User():
    print(request.form)
    if User.validate(request.form):
        data = {
            **request.form,
            'user_id': session['id']
        }
        print(data)
        User.create_User(data)
        return redirect('/dashboard')
    return redirect('/Users/new')

@app.route('/Users/<int:id>')
def show_User(id):
    if 'id' not in session:
        return redirect('/')
    User = User.get_User_by_id({'id':id})
    user = User.get_user_by_id(session)
    return render_template("show_user.html", User = User, user = user)

@app.route('/delete/<int:id>', methods= ['POST'])
def destroy(id):
    if 'id' not in session:
        return redirect('/')
    User.destroy({'id':id})
    return redirect('/dashboard')