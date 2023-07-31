# Import necessary modules from the Flask library
from flask import redirect, session, render_template

# Import the 'wraps' function from the 'functools' library
from functools import wraps

# Define a function called 'apology' that takes a 'message' and an optional 'code' parameter (default value: 400)
def apology(message, code=400):
    """Render message as an apology to user."""

    # Define an internal function 'escape' that takes a string 's'
    # This function escapes special characters in the given string following the provided replacements
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        # Define a list of tuples with pairs of old and new characters to be replaced
        # The function will replace occurrences of old characters with new characters in the string 's'
        special_characters = [
            ("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
            ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")
        ]

        # Iterate through the list of special characters and replace them in the string 's'
        for old, new in special_characters:
            s = s.replace(old, new)

        return s

    # Return the rendered template 'apology.html' with the 'message' and 'code' passed as variables
    # The 'message' will be escaped using the 'escape' function before rendering
    return render_template("apology.html", top=code, bottom=escape(message)), code

# Define a function decorator called 'login_required' that takes a function 'f' as input
def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """

    # Define an internal function called 'decorated_function' that accepts any number of arguments and keyword arguments
    # The 'wraps' decorator ensures that the original function's metadata is preserved (e.g., name, docstring)
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the 'user_id' key exists in the 'session' dictionary
        if session.get("user_id") is None:
            # If the user is not logged in, redirect them to the login page
            return redirect("/login")

        # If the user is logged in, call the original function 'f' with the provided arguments and keyword arguments
        return f(*args, **kwargs)

    # Return the 'decorated_function' to be used as a decorator for other routes that require login
    return decorated_function
