from flask import jsonify
from flask import Flask
from werkzeug.exceptions import HTTPException

def not_found(_: HTTPException):
    return jsonify({"error": "Endpoint not found", "status": "error"}), 404

def internal_error(_: Exception):
    return jsonify({"error": "Internal server error", "status": "error"}), 500

def register_error_handlers(app: Flask) -> None:
    app.register_error_handler(404, not_found)
    app.register_error_handler(500, internal_error)

