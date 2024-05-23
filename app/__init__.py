import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config 
from .swagger import configure_swagger

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    try:
        db.init_app(app)
        migrate.init_app(app, db)

        configure_swagger(app)
        from .routes.task_routes import task_bp
        app.register_blueprint(task_bp)

        return app
    except Exception as e:
        logging.error(f"Error initializing the application: {e}")
        return None
