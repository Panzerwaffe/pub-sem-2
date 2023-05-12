from flask import Flask, request, redirect, url_for
from .models import Some, db

app = Flask(__name__)

# routes
@app.route('/', methods=['GET'])
def index():
	dat = Some.query.all()
	return ",".join(d.text for d in dat)


@app.route('/create', methods=['GET', 'POST'])
def add_some():
	if request.method == "POST":
		text = request.form.get("text", type=str)

		some = Some(text=text)
		db.session.add(some)
		db.session.commit()

		return redirect(url_for('index'))

	return "create page"

