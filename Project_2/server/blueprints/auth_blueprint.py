from flask import Blueprint, request, jsonify
from flask_cors import CORS

auth_bp = Blueprint('auth', __name__)
CORS(auth_bp)

users = {
    "testuser": "password123"
}

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'Username already exists'}), 400

    users[username] = password
    return jsonify({'message': 'Registration successful'}), 201