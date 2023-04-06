from . import db
from sqlalchemy.sql import func


class Something(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	rating = db.Column(db.Integer)
	created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

	def __repr__(self):
		return f'Dude stuff {self.name}'