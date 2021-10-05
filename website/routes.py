from flask import Blueprint, render_template
from flask_login import login_required, current_user

# creates a blueprint object of all the routes on the website
routes = Blueprint('routes', __name__)


# ('/') defines the root route after the url
@routes.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)
