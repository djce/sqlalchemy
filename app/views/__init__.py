from .test import test_bp
from .user import user_bp
from .ady import ady_bp

def init_app(app):
    app.register_blueprint(test_bp, url_prefix='/test')
    app.register_blueprint(user_bp, url_prefix='/')
    app.register_blueprint(ady_bp, url_prefix='/')