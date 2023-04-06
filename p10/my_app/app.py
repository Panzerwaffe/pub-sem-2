from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = 'secret!'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.sqlite"

Session(app)
db.init_app(app)
print('re init')

