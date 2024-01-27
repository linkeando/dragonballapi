from DragonBall.Data import Characters

from flask import Blueprint, request, make_response, jsonify

character_blueprint = Blueprint('character', __name__)


@character_blueprint.route("/information" + "/<string:character_name>")
def character(character_name):
    character_name = Characters.Characters(character_name).character_information()
    return make_response(jsonify(character_name), 200)


@character_blueprint.route("/information-list", methods=["POST"])
def characters():
    data_list = request.json.get("characters", [])
    return make_response(jsonify(Characters.Characters.character_list(data_list)), 200)


@character_blueprint.route("/list")
def list_characters():
    return Characters.Characters.list()


def init_app(app):
    app.register_blueprint(character_blueprint)
