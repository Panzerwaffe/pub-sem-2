import requests
from flask import Flask, request, render_template, redirect
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

host = "127.0.0.10"
port = 10000

# just for example
# DO NOT USE IT IN PRODUCTION!
user_db = {
	'user': '1234',
	'admin': 'admin'
}

apps_id = {
	'12345678': 'normalno, svoyi'
}

token_db = {

}


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')

		# just for demonstration
		# always use a hash!
		if user_db.get(username) == password:

			# check if login via token
			app_id = request.form.get('app_id')
			url_redirect = request.form.get('url_redirect')

			if apps_id.get(app_id) and url_redirect:
				# !!!
				params = dict(code='GENERATE CODE...')

				req = requests.Request('GET', url_redirect, params=params).prepare()
				return redirect(req.url)

			# classic login
			return 'classic login, do not implement'

	# if it is non-classic way to login (via token)
	if 'app_id' in request.args:
		app_id = request.args.get('app_id')
		url_redirect = request.args.get('url_redirect')
		return render_template('login.html', app_id=app_id, url_redirect=url_redirect)

	# classic login either
	return 'classic login, do not implement'



# class GenerateToken(Resource):
# 	def post(self):
# 		data user code
# 		if user code == user code in session OR hardcoded
# 		return token as json

# class UserInfo(Resource):
# 	def post(self):
# 		return some user info
#       if request TOKEN is the same token for user in our DB -> retrun data
#       else error

# api.add_resource(GenerateToken, '/api/access_token')
# api.add_resource(GenerateToken, '/api/user_info')

if __name__ == '__main__':
	app.run(host=host, port=port)