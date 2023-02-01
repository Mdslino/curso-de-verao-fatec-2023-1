import logging

from flask import jsonify
from flask_restful import Resource

logger = logging.getLogger(__name__)


class HealthCheckResource(Resource):
    def get(self):
        logger.info("Health check endpoint called.")
        return jsonify({"status": "ok"})
