import subprocess
import json
from config import Config

def call_binary(prompt: str) -> dict:
    # Call C++ binary with prompt and parse JSON output
    try:
        result = subprocess.run(
            [str(Config.BINARY_PATH), str(Config.MODEL_PATH), str(prompt)],
            capture_output=True,
            text=True,
            timeout=Config.GENERATION_TIMEOUT,
            check=True,
        )
        return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        raise Exception(f"Generation timeout after {Config.GENERATION_TIMEOUT}s")
    except json.JSONDecodeError as e:
        raise Exception(f"Invalid JSON from binary: {e}")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Binary error (exit code {e.returncode}): {e.stderr}")

