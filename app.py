from flask import Flask
from datetime import datetime
import re
from flask import render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/product/")
def product():
    return render_template("product.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/login/")
def login():
    return render_template("login.html")
