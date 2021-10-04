# setup for flask app
from flask import Flask


# creates the flask app
def create_app():
    app = Flask(__name__)
    # for session cookies and other info
    app.config['SECRET_KEY'] = 'secret key for cookies'

    from .routes import routes
    from .auth import auth

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
