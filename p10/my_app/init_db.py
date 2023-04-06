from app import app, db
from models import User

def init_db():
	with app.app_context():
		db.create_all()

		# fill the database if you need
		# u = User(username='example4')
		# db.session.add(u)
		# db.session.commit()

		for user in User.query.all():
			print(user)


if __name__ == '__main__':
	init_db()