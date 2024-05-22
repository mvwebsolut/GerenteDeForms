from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.firebase_service import FirebaseHandler

database = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
firebase_handler = FirebaseHandler()