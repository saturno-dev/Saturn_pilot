import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config.from_json('../config.json')
db = SQLAlchemy(app)


# RUTAS ESTATICAS
@app.route("/") 
def index():
    return "hola CRUD"


if __name__ == "__main__":
    app.run(debug=True)
