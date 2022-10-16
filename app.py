from math import e
from flask import Flask, request, render_template, session
from datetime import datetime
import re
import json


class User():
    def __init__(self, name, email, psw):
        self.name = name
        self.email = email
        self.psw = psw


app = Flask(__name__)
app.secret_key = 'qeqweqwqk24e21cjn!Ew@@dsa5'

path = "userStore.json"


def write_json(json_data):
    with open(path, 'w') as file_out:
        json.dump(json_data, file_out)


def read_json():
    with open(path) as file_in:
        return json.load(file_in)


def addUser(user):
    existing_json = read_json()
    u = existing_json.get(user.email)
    if u == None:
        existing_json[user.email] = user.__dict__
        write_json(existing_json)
        return True
    else:
        return False


def getUser(email):
    existing_json = read_json()
    return existing_json.get(email)


@app.route("/")
def home():
    return render_template("home.html", user=session.get('user'))


@app.route("/product/")
def product():
    fileObject = open("static/data.json", "r")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    smoothies = [a for a in aList if a['type'] == 'smoothies']
    salad = [a for a in aList if a['type'] == 'salad']
    bowl = [a for a in aList if a['type'] == 'bowl']
    return render_template("product.html", smoothies=smoothies, salad=salad, bowl=bowl, user=session.get('user'))


@app.route("/about/")
def about():
    return render_template("about.html", user=session.get('user'))


@app.route("/login/")
def login():
    return render_template("login.html", user=None)


@app.route("/logout/")
def logout():
    if 'user' in session:
        session.pop('user', None)
    return render_template("home.html", user=None, msg="User Successfully Logged out !!")


@app.route("/signin_action", methods=['POST'])
def signIn():
    email = request.form['email']
    psw = request.form['psw']
    user = getUser(email=email)
    if user == None:
        return render_template("login.html", user=None, msg="User does not exsist, please use sign up to create account")
    else:
        if user['psw'] != psw:
            return render_template("login.html", user=None, msg="Credentials do not match, please try again ")
        else:
            session['user'] = user
            return render_template("home.html", user=user)


@app.route("/signup_action", methods=['POST'])
def signUp():
    email = request.form['email']
    name = request.form['name']
    psw = request.form['psw']
    user = User(name, email, psw)
    if addUser(user=user):
        user_json = json.loads(json.dumps(user.__dict__))
        session['user'] = user_json
        return render_template("home.html", user=user_json)
    else:
        return render_template("login.html", user=None, msg="User already Exist try adding new user")
