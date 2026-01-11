from flask import Blueprint, jsonify
from config import Config

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "owasp-llm-api",
        "binary_path": Config.BINARY_PATH,
        "model_path": Config.MODEL_PATH
    })

