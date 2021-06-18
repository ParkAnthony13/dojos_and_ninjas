from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template('ninja_page.html',dojos=dojos)

@app.route('/ninjas/post',methods=['POST'])
def new_ninja():
    data = {
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_options']
    }
    Ninja.insert(data)
    dojo_number = request.form['dojo_options']
    return redirect(f'/dojos/{dojo_number}')