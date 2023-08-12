from flask import Blueprint, jsonify, request, render_template
from user import User
import bcrypt

users_bp = Blueprint('users', __name__)

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

@users_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    password = data.get('encrypt_pass')
    secret = hash_password(password)
    new_user = User.create(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        email=data.get('email'),
        encrypt_pass=secret
    )
    return jsonify({
        "last_name": new_user.last_name,
        "first_name": new_user.first_name,
        "email": new_user.email    
    }), 201
