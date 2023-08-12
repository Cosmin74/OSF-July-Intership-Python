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
    ok = 0
    last_name = request.form.get('last_name')
    first_name = request.form.get('first_name')
    email = request.form.get('email')
    password = request.form.get('pass')
    secret = hash_password(password)
    new_user = User(
        first_name= first_name,
        last_name= last_name,
        email= email,
        encrypt_pass=secret
    )
    new_user.save()
    ok = 1
    return render_template('register.html', ok= ok)

@users_bp.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')


@users_bp.route('/authentification', methods=['GET'])
def login_user():
    users = list(User.select())
    return jsonify([{"id": user.user_id, "first_name": user.first_name, "last_name": user.last_name, "email": user.email} for user in users])
    