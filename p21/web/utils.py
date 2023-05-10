import random
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .models import Some

def fill_database(app: Flask, db: SQLAlchemy):
    with app.app_context():
        # fill the db
        some = Some(text=f"#->{random.random()}")
        db.session.add(some)
        db.session.commit()

def init_database(app: Flask, db: SQLAlchemy):
    with app.app_context():
        # create db with models imported above
        db.create_all()