from flask import Flask, request, redirect, url_for, jsonify
from utils import *

app = Flask(__name__)

host = "127.0.0.1"
port = 10001
url_redirect = f"http://{host}:{port}/authorization"

users = []

@app.route("/")
def index():
	print(users)
	return f"privet"

@app.route("/authorization")
def auth():
	code = request.args.get("code")
	if code is None:
		return redirect(url_for('index'))
	token = get_token_by_code(code, url_redirect)
	username, email = get_user_info(token)
	users.append((username, email, token))
	return redirect(url_for('index'))

@app.route("/login")
def login():
	# fast example
	link = generate_link(url_redirect)
	return redirect(link)



if __name__ == "__main__":
	app.run(host=host, port=port)