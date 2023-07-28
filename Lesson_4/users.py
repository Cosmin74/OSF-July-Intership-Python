from flask import Blueprint, jsonify, request
from models import User
from peewee import JOIN

users_bp = Blueprint('deapartment', __name__)

@users_bp.route('/department', methods=['GET'])
def get_users():
    users = list(User.select())
    return jsonify([{"id": user.dept_id, "name": user.dept_name} for user in users])

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_or_none(User.dept_id == user_id)
    if user:
        return jsonify({"id": user.dept_id, "name": user.dept_name})
    else:
        return jsonify({"error": "User not found"}), 404
    
@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    dept_name = data.get('dept_name')

    if not dept_name:
        return jsonify({"error": "dept_name is a required field"}), 400

    new_user = User.create(dept_name=dept_name)
    return jsonify({"dept_id": new_user.id, "dept_name": new_user.dept_name}), 201

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.get_or_none(User.dept_id == user_id)
    if user:
        data = request.get_json()
        user.dept_name = data.get('name', user.dept_name)
        user.save()
        return jsonify({"dept_id": user.dept_id, "dept_name": user.dept_name})
    else:
        return jsonify({"error": "User not found"}), 404

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.get_or_none(User.dept_id == user_id)
    if user:
        user.delete_instance()
        return jsonify({"message": "User deleted"})
    else:
        return jsonify({"error": "User not found"}), 404