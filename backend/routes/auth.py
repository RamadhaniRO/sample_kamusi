from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    User.create_user(email, password)
    return jsonify({"message": "User created"}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.find_user(email)
    if not user or not bcrypt.check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=email)
    return jsonify({"token": access_token}), 200
