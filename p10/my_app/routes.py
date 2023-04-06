from flask import redirect, render_template, url_for

from models import User

class UserRoutes:
	def __init__(self, app):
		self.app = app
		self.app.add_url_rule('/', view_func=self.index)

	@staticmethod
	def index():
		print('ok')
		users = User.query.all()
		return render_template('main.html', users=users)

