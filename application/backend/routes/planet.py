from DragonBall.Data import Planets

from flask import Blueprint, request, make_response, jsonify

planet_blueprint = Blueprint('planets', __name__)


@planet_blueprint.route("/information" + "/<string:planet_name>")
def planet(planet_name):
    planet_name = Planets.Planets(planet_name).planet_information()
    return make_response(jsonify(planet_name), 200)


@planet_blueprint.route("/information-list", methods=["POST"])
def planets():
    data_list = request.json.get("planets", [])
    return make_response(jsonify(Planets.Planets.planet_list(data_list)), 200)


@planet_blueprint.route("/list")
def list_planets():
    return Planets.Planets.list()


def init_app(app):
    app.register_blueprint(planet_blueprint)
