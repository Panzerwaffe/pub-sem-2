from app import db

class User(db.Model):
	# query: db.Query
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, nullable=False)

	def __repr__(self):
		return f"USER: {self.username}"
