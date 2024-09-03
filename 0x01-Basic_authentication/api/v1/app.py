#!/usr/bin/env python3
"""
Route module for the API
calls
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found() -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized() -> str:
    """ unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbiden() -> str:
    """user not allowed to access
    resource error
    """
    return jsonify({"error": "Forbiden"}), 403


if __name__ == "__main__":
    host: str = getenv("API_HOST", "0.0.0.0")
    port: int = getenv("API_PORT", 5000)
    app.run(host=host, port=port)
