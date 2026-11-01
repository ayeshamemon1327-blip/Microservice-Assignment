
from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# Generate three API keys for three consumers
api_keys = {
    "Consumer 1": secrets.token_urlsafe(24),
    "Consumer 2": secrets.token_urlsafe(24),
    "Consumer 3": secrets.token_urlsafe(24)
}

# Display generated keys in terminal
print("\nGenerated API Keys:")
for consumer, key in api_keys.items():
    print(f"{consumer}: {key}")


# Protected API endpoint
@app.route("/api/data", methods=["GET"])
def get_data():

    api_key = request.headers.get("X-API-Key")

    if not api_key:
        return jsonify({"error": "API key is missing"}), 401

    if api_key not in api_keys.values():
        return jsonify({"error": "Invalid API key"}), 403

    return jsonify({
        "message": "Access granted!",
        "data": "Welcome to the protected API."
    }), 200


if __name__ == "__main__":
 app.run(debug=True, port=5001, use_reloader=False)
