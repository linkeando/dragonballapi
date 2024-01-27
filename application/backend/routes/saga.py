from DragonBall.Data import Sagas

from flask import Blueprint, request, make_response, jsonify

saga_blueprint = Blueprint('saga', __name__)


@saga_blueprint.route("/information" + "/<string:saga_name>")
def saga(saga_name):
    saga_name = Sagas.Sagas(saga_name).saga_information()
    return make_response(jsonify(saga_name), 200)


@saga_blueprint.route("/information-list", methods=["POST"])
def sagas():
    data_list = request.json.get("sagas", [])
    return make_response(jsonify(Sagas.Sagas.saga_list(data_list)), 200)


@saga_blueprint.route("/list")
def list_sagas():
    return Sagas.Sagas.list()


def init_app(app):
    app.register_blueprint(saga_blueprint)
