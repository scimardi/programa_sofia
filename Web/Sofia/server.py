from flask import Flask, render_template, request, redirect, url_for, session
from Pessoa import *

app = Flask("__name__")
app.config["SECRET_KEY"] = 'admin'

@app.route("/")
def iniciar():
    return render_template("inicio.html")