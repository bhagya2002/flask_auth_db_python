from flask import Blueprint

# creates a blueprint object of all the routes on the website
routes = Blueprint('routes', __name__)


# ('/') defines the root route after the url
@routes.route('/')
def home():
    return 'Hello World!'
