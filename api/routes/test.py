from flask import Blueprint, request, jsonify, current_app
from binary import call_binary
from config import Config

test_bp = Blueprint('test', __name__)

@test_bp.route('/api/test', methods=['POST'])
def test_prompt():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "Missing 'prompt' field in request body"}), 400

    if len(prompt) > Config.MAX_PROMPT_LENGTH:
        return jsonify({
            "error": f"Prompt too long (max {Config.MAX_PROMPT_LENGTH} chars)"
        }), 400

    try:
        result = call_binary(prompt)
        return jsonify(result), 200
    except Exception as e:
        current_app.logger.error(f"Error processing prompt: {e}")
        return jsonify({"error": str(e), "status": "error"}), 500

