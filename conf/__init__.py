from .settings import DevelopmentConfig,ProductionConfig
import os

def load_config(mode=os.getenv('FLASK_CONFIG')):
    if mode == 'dev':
        return DevelopmentConfig
    elif mode == 'prod':
        return ProductionConfig
    else:
        return DevelopmentConfig