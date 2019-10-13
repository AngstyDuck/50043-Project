from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db


def make_app(config='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config)

    CORS(app, supports_credentials=True)

    # DB setup
    db.init_app(app)
    Migrate(app, db)

    # Define modules
    from app.modules import endpoint_folder_1
    app.register_blueprint(endpoint_folder_1.module)

    return app
