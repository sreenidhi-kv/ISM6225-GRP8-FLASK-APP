from flask import Flask
from datetime import datetime
import re
from flask import render_template
import json


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/product/")
def product():
    fileObject = open("static/data.json", "r")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    smoothies = [a for a in aList if a['type'] == 'smoothies']
    salad = [a for a in aList if a['type'] == 'salad']
    bowl = [a for a in aList if a['type'] == 'bowl']
    return render_template("product.html", smoothies=smoothies, salad=salad, bowl=bowl)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/login/")
def login():
    return render_template("login.html")
