# Import required libraries
import os
from flask import Flask, flash, redirect, request, session
from flask_session import Session
from routes import register_routes

# Create a Flask web application instance
app = Flask(__name__)

# Configure session to use the filesystem for storing session data
# Instead of using signed cookies, this configuration stores session data in files on the server's filesystem.
# This is useful for small-scale applications and local development.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Define an after_request handler to modify the response headers for caching prevention.
# This ensures that responses won't be cached by browsers or intermediaries.
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Register routes from the 'routes' module to the app instance
# The 'register_routes' function is responsible for defining all the routes and their handlers.
register_routes(app)

# Start the application if this script is being run as the main program
# 'debug=True' enables debug mode for the Flask app, which is useful during development.
# In debug mode, the app will automatically reload when code changes are detected,
# and it will provide more detailed error messages for easier debugging.
if __name__ == '__main__':
    app.run(debug=True)
