"""
Flask application entry point
Initializes the Flask app, extensions, routes, and launches the server
"""

# Import Flask and extensions
from flask import Flask, redirect, url_for, render_template

# Import configuration
from config import Config

# Initialize extensions
from extensions import db


# Create and configure Flask app
def create_app():
    """Initialize Flask app and register all extensions and blueprints"""
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object(Config)
    
    # Initialize SQLAlchemy with the app
    db.init_app(app)
    
    
    # Register blueprints from routes/
    from routes.auth import auth_bp
    from routes.achievements import achievements_bp
    from routes.staff import staff_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(achievements_bp)
    app.register_blueprint(staff_bp)
    
    # Root route redirects to login page
    @app.route("/")
    def index():
        """Homepage redirects to login"""
        return render_template("index.html")
    
    return app


# Create app instance
app = create_app()


# Run the app with debug mode if executed directly
if __name__ == "__main__":
    app.run(debug=True)
