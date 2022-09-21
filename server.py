from flask import render_template, session, redirect,request
from flask_crud import app
from flask_crud.controllers import ninjas, dojos

if __name__=="__main__":
    app.run(debug=True)
