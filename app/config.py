class DebugConfig:

    SECRET_KEY = "mateus123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///debug_database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig:
    SECRET_KEY = "mateus123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///production_database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    