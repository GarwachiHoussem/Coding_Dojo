from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.party import Party

@app.route('/parties/new')
def new_party():
    if not "user_id" in session:
        return redirect("/")
    return render_template("new_party.html")


@app.route('/parties/create', methods=['post'])
def create_party():
    if Party.validate(request.form):
        data = {**request.form, "user_id": int(session["user_id"])}
        db_return = Party.create(data)
        print(db_return)
        return redirect('/dashbord')
    return redirect('/parties/new')
