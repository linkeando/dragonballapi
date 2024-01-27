from flask import Blueprint, render_template

from application.flask_app import FlaskApp

home_bp = Blueprint('home', __name__)
cache = FlaskApp().cache


@home_bp.route('/', methods=['GET'])
@cache.cached(timeout=86400)
def home_page():
    return render_template("index.html")


def init_app(app):
    app.register_blueprint(home_bp)
