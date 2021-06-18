from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojo_page.html',dojos = dojos)

@app.route('/dojos/post',methods=['POST'])
def new_dojo():
    data = {
        'name':request.form['new_dojo']
    }
    Dojo.insert(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    something=Dojo.dojo_class({'dojo_id':dojo_id})
    return render_template('one_dojo.html',something=something)