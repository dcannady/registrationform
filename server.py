from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile('^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def process():
    session["error"] = []
    if len(request.form['email']) < 1:
        session["error"].append("Field must be a match")
    # else if email doesn't match regular expression display an "invalid email address" message
    elif not EMAIL_REGEX.match(request.form['email']):
        # We are using the EMAIL_REGEX object that we created and running the "match" method that will return a boolean indicating whether the argument matches.
        session("Invalid Email Address!")
    else:
        flash("Success!")
    info = {
    "email": request.form['email'],
    "first name": request.form['first_name'],
    "last name": request.form['last_name'],
    "password": request.form['password'],
    "confirm password": request.form['confirm_password']
    }
    # len(info["first name"])
    if len(request.form['password']) > 8:
        session["error"].append("Password should be more than 8 characters")
    if len(request.form['first_name']) < 1:
        session["error"].append("Field must not be blank!")
    elif not request.form['first_name'].isalpha():
        session["error"].append("Contents cannot contain numbers!")
    if len(request.form['last_name']) < 1:
        session["error"].append("Field must not be blank!")
    if len(request.form['password']) < 1:
        session["error"].append("Field must not be blank!")
    if len(request.form['confirm_password']) < 1:
        session["error"].append("Field must not be blank!")
    if request.form["password"] == request.form["confirm_password"]:
        session["error"].append("Password and Password Confirmation should match!")
    print session["error"]
    flash(session["error"])
    return redirect("/")
app.run(debug=True)
