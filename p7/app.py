from flask import Flask, render_template, session
from flask_session import Session
from ws.app import MyWebSocket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)
socket = MyWebSocket(app)

users = {
	'user': '1',
	'user2': '2',
}
history = {
	'1': [],
	'2': []
}

i = 0

@app.route('/')
def index():
	session['user'] = '????'
	return render_template('main.html')


if __name__ == '__main__':
	socket.run(app, allow_unsafe_werkzeug=True)