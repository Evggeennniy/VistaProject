from flask import Flask

app = Flask(__name__)


def create_app() -> Flask:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['UPLOAD_FOLDER'] = 'media/'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    from app import models, routers
    from flask_migrate import Migrate

    migrate = Migrate(app, models.db)

    return app
