from DragonBall.Data import Fusions

from flask import Blueprint, request, make_response, jsonify

fusion_blueprint = Blueprint('fusion', __name__)


@fusion_blueprint.route("/information" + "/<string:fusion_name>")
def fusion(fusion_name):
    fusion_name = Fusions.Fusions(fusion_name).fusion_information()
    return make_response(jsonify(fusion_name), 200)


@fusion_blueprint.route("/information-list", methods=["POST"])
def fusions():
    data_list = request.json.get("fusions", [])
    return make_response(jsonify(Fusions.Fusions.fusion_list(data_list)), 200)


@fusion_blueprint.route("/list")
def list_fusions():
    return Fusions.Fusions.list()


def init_app(app):
    app.register_blueprint(fusion_blueprint)
