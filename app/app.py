from flask import Flask

from app.config import DebugConfig
from app.extensions import (
    database,
    migrate,
    login_manager,
    firebase_handler
)
from app.routes import (
    webhook_route,
    home_route
)

app_config = DebugConfig()

def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config)
    #activate_extensions(app)
    register_routes(app)
    return app

def activate_extensions(app: Flask):
    login_manager.init_app(app)
    database.init_app(app)
    migrate.init_app(app, database)
    return

def register_routes(app: Flask):
    app.register_blueprint(webhook_route)
    app.register_blueprint(home_route)
    return
