from flask import Flask
from sqlalchemy import create_engine
from pathlib import Path
from conf import load_config
from .utils import JSONEncoder

BASE_DIR = Path(__file__).resolve().parent.parent

def create_app():

    app = Flask(__name__,
                template_folder=str(BASE_DIR / 'templates'),
                static_folder=str(BASE_DIR / 'static'))

    app.config.from_object(load_config())

    # 替换默认JSONEncoder
    app.json_encoder = JSONEncoder

    register_extensions(app)

    from . import views
    views.init_app(app)

    return app

def register_extensions(app: Flask) -> None:

    from .extensions import session, Base
    engine = create_engine(app.config['SQLALCHEMY_BINDS']['default'])

    # sqlite
    # engine = create_engine(
    #     app.config['SQLALCHEMY_DATABASE_URI'],
    #     connect_args={'check_same_thread': False})

    session.configure(bind=engine)

    from . import models
    Base.metadata.create_all(engine)