from flask import Flask
from flask_cors import CORS
from config import Config
from routes import health_bp, test_bp
from error import register_error_handlers

app = Flask(__name__)
CORS(app)

try:
    Config.validate()
except (ValueError, FileNotFoundError) as e:
    print(f"❌ Configuration error: {e}")
    exit(1)

# Register routes and error handlers
app.register_blueprint(health_bp)
app.register_blueprint(test_bp)
register_error_handlers(app)

if __name__ == '__main__':
    print(f"Starting OWASP LLM API Server")
    print(f"\tEnvironment: {Config.FLASK_ENV}")
    print(f"\tPort: {Config.FLASK_PORT}")
    print(f"\tDebug: {Config.FLASK_DEBUG}\n")

    app.run(
        host='0.0.0.0',
        port=Config.FLASK_PORT,
        debug=Config.FLASK_DEBUG
    )

