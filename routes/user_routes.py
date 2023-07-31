from flask import Blueprint, jsonify, request
from models.user import User
import sqlite3


user_bp = Blueprint('user', __name__)


@user_bp.route('/users', methods=['GET'])
def get_users():
    # Todo
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    users = [User(id=row[0], username=row[1], email=row[2]) for row in data]
    conn.close()
    return jsonify(users=[user.__dict__ for user in users]), 200


@user_bp.route('/users', methods=['POST'])
def add_user():
    # Todo
    data = request.get_json()
    username = data['username']
    email = data['email']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
    conn.commit()
    conn.close()

    return jsonify(message="User added successfully"), 201


