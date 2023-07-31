# Import necessary modules from Flask and other packages
import sqlite3
from cs50 import SQL
from flask import Blueprint, request, session, redirect, render_template, flash, g
from utils.http_code import HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST
from models.user import User
from utils.helpers import apology, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from db import DATABASE

# Create a Blueprint object named 'auth_bp' to define routes for authentication-related tasks
auth_bp = Blueprint('auth', __name__)

# Create an instance of the 'SQL' class to interact with the SQLite database
db = SQL(f"sqlite:///{DATABASE}")

# Define a route for handling both GET and POST requests to '/login'
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id to ensure a clean session
    session.clear()

    # Check if the user submitted the login form via POST (i.e., logging in)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", HTTP_403_FORBIDDEN)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", HTTP_403_FORBIDDEN)

        # Query database for the user's data based on the provided username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct by comparing hashes
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", HTTP_403_FORBIDDEN)

        # If the user is authenticated, store the user_id and username in the session
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to the homepage after successful login
        return redirect("/")

    # If the user reached the route via GET (i.e., accessing the login page directly)
    else:
        return render_template("login.html")

# Define a route for handling both GET and POST requests to '/register'
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id to ensure a clean session
    session.clear()

    # Retrieve data from the registration form
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")

    # Check if the user submitted the registration form via POST (i.e., registering)
    if request.method == "POST":
        # Check if the username was provided
        if not username:
            return apology("Must provide username", HTTP_400_BAD_REQUEST)

        # Check if the password was provided
        elif not password:
            return apology("Must provide password", HTTP_400_BAD_REQUEST)

        # Check if the password confirmation was provided
        elif not confirmation:
            return apology("Must confirm password", HTTP_400_BAD_REQUEST)

        # Ensure the password and confirmation match
        elif password != confirmation:
            return apology("Passwords must match", HTTP_400_BAD_REQUEST)

        # Query the database for any existing users with the provided username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure the username does not already exist
        if len(rows) != 0:
            return apology("Username already exists", HTTP_400_BAD_REQUEST)

        # Insert the new user into the database
        db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)",
            username, generate_password_hash(password)
        )

        # Query the database for the newly inserted user
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # If the registration is successful, store the user_id and username in the session
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to the homepage after successful registration
        return redirect("/")

    # If the user reached the route via GET (i.e., accessing the registration page directly)
    else:
        return render_template("register.html")

# Define a route for handling both GET and POST requests to '/update-password'
@auth_bp.route("/update-password", methods=["GET", "POST"])
def update_password():
    """Update password"""
    # Retrieve data from the password update form
    username = request.form.get("username")
    old_password = request.form.get("old_password")
    new_password = request.form.get("new_password")
    confirmation = request.form.get("confirmation")

    print(new_password)

    # Check if the user submitted the password update form via POST
    if request.method == "POST":
        # Query the database for the user's data based on the session's user_id
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        # Check if the username was provided
        if not username:
            flash("Username must be provided")
            return render_template("update-password.html")

        # Check if the new password was provided
        elif not new_password:
            flash("New Password must be provided")
            return render_template("update-password.html")

        # Ensure the password and confirmation match
        elif new_password != confirmation:
            flash("Passwords must match")
            return render_template("update-password.html")

        # Ensure the new password is different from the old password
        if len(rows) != 1 or old_password == new_password:
            flash("Invalid password")
            return render_template("update-password.html")

        # Update the user's password
        try:
            db.execute(
                "UPDATE users SET hash = :new_password WHERE username = :username",
                new_password=generate_password_hash(new_password),
                username=username,
            )
        except Exception as error:
            print(error)

        # Query the database for the newly updated user
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Store the updated user_id in the session
        session["user_id"] = rows[0]["id"]

        # Redirect user to the homepage after successfully updating the password
        flash("Password has been changed!")
        return redirect("/")

    # If the user reached the route via GET (i.e., accessing the update password page directly)
    else:
        return render_template("update-password.html")

# Define a route for handling GET requests to '/logout'
@auth_bp.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id to log the user out
    session.clear()

    # Redirect user to the login form after logging out
    return redirect("/")
