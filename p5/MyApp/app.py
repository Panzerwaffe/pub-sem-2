import requests
from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

host = "127.0.0.1"
port = 10000
url_redirect = f"http://{host}:{port}/authorization"
# just imitate oAuth with GitHub
app_id = 12345678
app_secret = 00000000

@app.route("/authorization")
def auth():
	# or in JSON
	code = request.args.get("code")
	# TODO
	# now send request to get token in JSON
	# and save it
	return f"прилетело из гита {code}"

@app.route("/")
def main():
	return render_template('main.html')

@app.route('/git_login')
def git_login():
	# double check that url exists :D
	git_auth_url = f'http://127.0.0.10:10000/login'
	params = dict(app_id=app_id, url_redirect=url_redirect)
	# just prepare URL, and NOT send it! Only prepare
	req = requests.Request('GET', git_auth_url, params=params).prepare()
	# redurect to GitHub page with our app data
	return redirect(req.url)

@app.route("/login", methods=['GET'])
def login():
	return render_template('login.html')


@app.route('/user')
def user():
	# show some user info via token
	return 'IMPLEMENT'

if __name__ == "__main__":
	app.run(host=host, port=port)