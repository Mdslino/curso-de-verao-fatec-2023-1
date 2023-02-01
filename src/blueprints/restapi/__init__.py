from flask import Blueprint
from flask_restful import Api

from src.blueprints.restapi.resources import HealthCheckResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(HealthCheckResource, "/healthcheck")
    app.register_blueprint(bp)
