from flask_crud import app
from flask_crud.models.dojo import Dojo
from flask import render_template, flash, session, redirect, request

@app.route('/dojos')
def all_dojos():
    all_dojos = Dojo.get_all()
    return render_template('index.html', all_dojos=all_dojos)
"""

"""
@app.route('/dojos', methods=['POST', 'GET'])
def add_dojos():
    if  request.method == 'GET':
        all_dojos = Dojo.get_all()
        return render_template("index.html", all_dojos = all_dojos)
    
    if  request.method == 'POST':
        
        data = {
            'name': request.form['name']
        }

        Dojo.save(data)
        return redirect( '/dojos')


@app.route("/dojos/<int:id>")
def dojo_detalle(id):
    data = {
        'dojos_id': id
    }
    dojo_ninjas = Dojo.get_dojo_ninjas(data)

    return render_template("dojo_show.html", dojo= dojo_ninjas)

@app.route('/dojos/eliminar/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Dojo.destroy(data)
    return redirect('/dojos')