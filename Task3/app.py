from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Secret key for JWT
SECRET_KEY = "my_secret_key"

# Employee records
employees = {
    "emp1": {
        "password": "123",
        "role": "employee"
    },
    "admin1": {
        "password": "admin123",
        "role": "admin"
    }
}


# Login API - Generate JWT Token
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = employees.get(username)

    if user and user["password"] == password:

        token = jwt.encode({
            "username": username,
            "role": user["role"],
            "exp": datetime.datetime.now(datetime.timezone.utc)
                   + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm="HS256")

        return jsonify({"token": token}), 200

    return jsonify({"error": "Invalid username or password"}), 401


# Token Verification
def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            token = token.replace("Bearer ", "")
            data = jwt.decode(
                token, SECRET_KEY, algorithms=["HS256"]
            )
            request.current_user = data

        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid or expired token"}), 401

        return f(*args, **kwargs)

    return decorated


# Employee Access
@app.route("/employee", methods=["GET"])
@token_required
def employee_access():

    return jsonify({
        "message": "Welcome Employee!",
        "user": request.current_user["username"]
    }), 200


# Admin Access
@app.route("/admin", methods=["GET"])
@token_required
def admin_access():

    if request.current_user["role"] != "admin":
        return jsonify({"error": "Admin access only"}), 403

    return jsonify({
        "message": "Welcome Admin!",
        "user": request.current_user["username"]
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5002, use_reloader=False)