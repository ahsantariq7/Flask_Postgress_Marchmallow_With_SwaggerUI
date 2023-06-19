import os
import pathlib

import connexion
from dotenv import load_dotenv

from src.db import init_db
from src.extensions import db, ma

load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASS = os.getenv("POSTGRES_PASS")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def create_app():
    # app = Flask(__name__)
    basedir = pathlib.Path(__file__).parent.resolve()
    connex_app = connexion.App(__name__, specification_dir=basedir)

    app = connex_app.app
    app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    register_extensions(app)

    with app.app_context():
        init_db()

    return connex_app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
