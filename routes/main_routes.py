# Import necessary modules from Flask and other packages
import sqlite3
from flask import Blueprint, jsonify, request, session, redirect, render_template
from utils.http_code import HTTP_403_FORBIDDEN
from utils.helpers import apology, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
from db import DATABASE

# Create a Blueprint object named 'main_bp' to define routes for the main app
main_bp = Blueprint('main', __name__)

# Create an instance of the 'SQL' class to interact with the SQLite database
db = SQL(f"sqlite:///{DATABASE}")

# Define a route for handling GET requests to '/'
@main_bp.route('/', methods=['GET'])
@login_required
def show():
    """Show overview of todos"""
    # Get user's todos from the 'todos' table in the database
    todos = db.execute(
        "SELECT * FROM todos WHERE user_id = :user_id",
        user_id=session["user_id"],
    )

    # Render the 'index.html' template with the fetched todos as context
    return render_template(
        "index.html",
        todos=todos
    )

# Define a route for handling POST requests to '/checked/<todo_id>'
@main_bp.route('/checked/<todo_id>', methods=['POST'])
@login_required
def mark_as_done(todo_id):
    """Mark todo as done"""
    # Get the 'is_checked' value from the submitted form data
    is_checked = int(request.form.get("is_checked"))
    if todo_id:
        # Update the 'completed' field for the specified todo based on the 'is_checked' value
        if is_checked:
            db.execute(
                "UPDATE todos SET completed = ? WHERE id = ?",
                0, todo_id,
            )
        else:
            db.execute(
                "UPDATE todos SET completed = ? WHERE id = ?",
                1, todo_id,
            )
        
    # Redirect the user to the homepage after marking the todo as done
    return redirect("/")

# Define a route for handling POST requests to '/delete/<todo_id>'
@main_bp.route('/delete/<todo_id>', methods=['POST'])
@login_required
def delete(todo_id):
    """Delete todo"""
    if todo_id:
        # Delete the specified todo from the 'todos' table in the database
        db.execute("DELETE FROM todos WHERE id = ?", todo_id)

    # Redirect the user to the homepage after deleting the todo
    return redirect("/")
