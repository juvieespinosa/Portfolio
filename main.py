from flask import Flask, render_template, redirect, url_for, request, flash, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from dotenv import load_dotenv

import smtplib
import os

load_dotenv()

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/download", methods=['GET', 'POST'])
def download_file():
    path = "juvie-rosarie-espinosa.pdf"
    return send_file(path, as_attachment=True)


if __name__ =="__main__":
    app.run(debug=True)