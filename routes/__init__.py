from flask import Flask

def register_routes(app: Flask):
    from .user_routes import user_bp
    from .todo_routes import todo_bp
    from .auth_routes import auth_bp
    from .main_routes import main_bp

    # Register blueprints with the app
    app.register_blueprint(user_bp)
    app.register_blueprint(todo_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

# This is a convention to keep the route registration separate from app creation
