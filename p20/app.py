import sys
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return "kek"

if __name__ == '__main__':
	print(sys.argv[1])
	app.run(host="0.0.0.0", port=8000)
