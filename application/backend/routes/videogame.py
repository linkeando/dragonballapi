from DragonBall.Data import VideoGames

from flask import Blueprint, request, make_response, jsonify

game_blueprint = Blueprint('game', __name__)


@game_blueprint.route("/information" + "/<string:game_name>")
def saga(game_name):
    game_name = VideoGames.VideoGames(game_name).game_information()
    return make_response(jsonify(game_name), 200)


@game_blueprint.route("/information-list", methods=["POST"])
def sagas():
    data_list = request.json.get("games", [])
    return make_response(jsonify(VideoGames.VideoGames.game_list(data_list)), 200)


@game_blueprint.route("/list")
def list_sagas():
    return VideoGames.VideoGames.list()


def init_app(app):
    app.register_blueprint(game_blueprint)
