from pathlib import Path
from dotenv import load_dotenv
from urllib import parse
import os

load_dotenv(verbose=True)
BASE_DIR = Path(__file__).resolve().parent.parent

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = parse.quote_plus(str(os.getenv('MYSQL_PASSWORD')))
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

class Config(object):

    JSON_AS_ASCII = False
    JSON_SORT_KEYS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SECRET_KEY = '_5#y2L"F4Q8z\n\xec]/'
    SQLALCHEMY_BINDS = {
        'default': f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4'
    }
    # SQLALCHEMY_DATABASE_URI = f"sqlite:///{str(BASE_DIR / 'dev.db')}"

class ProductionConfig(Config):
    pass