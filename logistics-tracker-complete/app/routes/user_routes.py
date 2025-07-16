from flask import Blueprint, request, jsonify, current_app
from app.auth.jwt_handler import encode_auth_token

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    current_app.db.users.insert_one(data)
    return jsonify({"message": "User registered successfully"})

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = current_app.db.users.find_one({"email": data['email']})
    if user:
        token = encode_auth_token(str(user['_id']))
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401
