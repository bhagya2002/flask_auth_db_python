from flask import Blueprint, render_template, request, flash, redirect, url_for
# Blurprint - helps create routes for different links/paths in a web app
# render_template - renders a html file
# request - allows us to get data from a form
# flash - allows us to display messages to the user (flash a message)

from .models import User  # get the User schema to update db
from werkzeug.security import generate_password_hash, check_password_hash
# generate_password_hash, used for hashing password in the db for security (convert from plain text to smth else)
# check_password_hash

from . import db

from flask_login import login_user, login_required, logout_user, current_user
# current_user is connected with UserMixin

# creates a blueprint object of all the routes on the website
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    # data = request.form  # get the data from the form, url data, etc.
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        # looking for a specific entry in the db and filtering by a certain column
        user = User.query.filter_by(email=email).first()
        if user:
            # if a user was found with the same email check the hashed password if it matches with the entered password
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                login_user(user, remember=True)  # logging in this user
                return redirect(url_for('routes.home'))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category='error')
        
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required  # makes sure the user is logged in to see the logout page
def logout():
    logout_user()  # logs the current user out
    return redirect(url_for("auth.login"))


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # find if user email already exists, error
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category='error')
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must be greator than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)  # logging in this user
            flash("Account created!", category="success")
            return redirect(url_for("routes.home"))

    return render_template('sign_up.html', user=current_user)
