from app.ext.db import db
from flask_migrate import Migrate

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)

   
