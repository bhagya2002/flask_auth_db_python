from flask import Blueprint, render_template, request, flash
# Blurprint - helps create routes for different links/paths in a web app
# render_template - renders a html file
# request - allows us to get data from a form
# flash - allows us to display messages to the user (flash a message)

# creates a blueprint object of all the routes on the website
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    # data = request.form  # get the data from the form, url data, etc.
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return '<p>logout</p>'


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(firstName) < 2:
            flash("First name must be greator than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters", category="error")
        else:
            flash("Account created!", category="success")

    return render_template('sign_up.html')
