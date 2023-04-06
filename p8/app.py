from flask import Flask, render_template, se
from ws.app import MyWebSocket
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)
socket = MyWebSocket(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, nullable=False)

with app.app_context():
	db.create_all()

	u = User(username='example2')
	db.session.add(u)
	db.session.commit()

	users = db.session.execute(db.select(User)).scalars()


@app.route('/')
def index():
	return render_template('main.html')


if __name__ == '__main__':
	socket.run(app, allow_unsafe_werkzeug=True)