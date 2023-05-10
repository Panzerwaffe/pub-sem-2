from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Some(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
