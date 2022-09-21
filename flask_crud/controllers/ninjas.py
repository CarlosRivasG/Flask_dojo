from flask_crud import app
from flask_crud.models.ninja import Ninja
from flask_crud.models.dojo import Dojo

from flask import render_template, flash, session, redirect, request

@app.route('/ninjas')
def all_ninjas():
    all_dojos= Dojo.get_all()
    return render_template('create_ninja.html', all_dojos=all_dojos)

@app.route('/ninjas/process', methods=['POST'])
def process_new_ninja():
    
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojos_id': request.form['dojos_id'],
    }
    new_ninja = Ninja.add_ninja(data)
    print("--->", data)
    if new_ninja != False:
        return redirect(f"/dojos/{request.form['dojos_id']}")
    flash(':/ Something broke, the Ninja could not be created', 'danger')
    return redirect('/dojos')

