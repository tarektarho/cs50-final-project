# Todo App

## Video Demo: <URL HERE>

## **Description:**

The Todo App is a simple web application that allows users to create, manage, and track their tasks (todos). It provides basic functionality for user authentication, registration, logging in, updating passwords, and logging out. Users can view their todos, mark them as done, and delete them.

### **Getting Started**

To run the Todo App on your local machine, follow the steps below:

### **Prerequisites**

- Python: Make sure you have Python installed on your system. You can download Python from the official website: Python Downloads.

- Flask: The Todo App is built using the Flask web framework. Install Flask using the following command:

```bash
pip install flask
```

- SQLite: The app uses SQLite as the database. SQLite usually comes pre-installed with Pyth

### **Installation**

- Clone the repository:

```bash
git clone https://github.com/your-username/todo-app.git
```

- Navigate to the project directory:

```bash
cd todo-app
```

- Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

- Activate the virtual environment:

  - On Windows:

  ```bash
  venv\Scripts\activate
  ```

  - On macOS and Linux:

  ```bash
  source venv/bin/activate
  ```

- Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### **Usage**

- Run the Flask app:

```basah
python app.py
```

- Open your web browser and visit http://localhost:5000 to access the Todo App.

### **Features**

The Todo App comes with the following features:

- User registration: New users can create an account to start using the app.
- User login: Registered users can log in to access their todos.
- User authentication: Certain routes require users to be logged in, which is - ensured using the login_required decorator.
- View todos: Logged-in users can view their todos on the homepage.
- Mark as done: Users can mark their todos as done, updating their status.
- Delete todos: Users can delete todos they no longer need.
- Update password: Users can change their account password.

### **Folder Structure**

- The Todo App follows a structured folder layout:
  ```arduino
  ├── app.py
  ├── db.py
  ├── requirements.txt
  ├── static/
  │   └── styles.css
  ├── templates/
  │   ├── addTodo.html
  │   ├── index.html
  │   ├── login.html
  │   ├── register.html
  │   └── update-password.html
  ├── utils/
  │   ├── helpers.py
  │   └── http_code.py
  ├── models/
  │   └── user.py
  ├── routes/
  │   ├── __init__.py
  │   ├── auth_routes.py
  │   └── todo_routes.py
  └── database.db
  ```

### **Contributing**

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

### **License**

The Todo App is open-source and is released under the **MIT License.** Feel free to use, modify, and distribute it according to the terms of the license.

### **Acknowledgments**

- The Todo App was inspired by the need for a simple and functional task management tool.
- The Flask web framework and SQLite database made it easy to develop the app quickly and efficiently.
