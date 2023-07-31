# Import necessary modules from Flask
from flask import Blueprint, request, render_template, session, redirect

# Import the 'apology' function from 'helpers' module
from utils.helpers import apology

# Import the 'DATABASE' constant and the 'SQL' class from 'db' module
from db import DATABASE
from cs50 import SQL

# Create a Blueprint object named 'todo_bp' to define todo-related routes
todo_bp = Blueprint('todo', __name__)

# Create an instance of the 'SQL' class to interact with the SQLite database
db = SQL(f"sqlite:///{DATABASE}")

# Define a route for handling GET requests to '/todos'
@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    # Fetch all todos associated with the current user from the 'todos' table
    todos = db.execute(
        "SELECT * FROM todos WHERE user_id = :user_id",
        user_id=session["user_id"],
    )

    # Cast the 'completed' field to boolean (True or False) for each todo
    for todo in todos:
        todo['completed'] = bool(todo['completed'])

    # Render the 'addTodo.html' template with the fetched todos as context
    return render_template("addTodo.html", todos=todos)

# Define a route for handling POST requests to '/todos'
@todo_bp.route('/todos', methods=['POST'])
def add_todo():
    # Get the value of 'task' from the submitted form data
    task = request.form.get("task")

    # Get the 'user_id' from the current user's session
    user_id = session["user_id"]

    # Set the 'completed' field to False for the new todo
    completed = False

    # If the 'task' field is empty, return an apology with status code 400 (Bad Request)
    if not task:
        return apology("Invalid symbol", 400)

    try:
        # Insert the new todo into the 'todos' table in the database
        db.execute("INSERT INTO todos (user_id, task, completed) VALUES (:user_id, :task, :completed)", user_id=user_id, task=task, completed=completed)
    except Exception as error:
        print(error)

    # Redirect the user to the '/todos' route after adding the todo
    return redirect("/todos")
