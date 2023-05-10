from flask import Flask
from .models import Some

app = Flask(__name__)

# routes
@app.route('/', methods=['GET'])
def index():
	dat = Some.query.all()
	return ",".join(d.text for d in dat)