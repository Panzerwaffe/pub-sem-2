import datetime
import numpy as np

from flask import Flask, Response, abort, redirect, render_template, request, url_for, session
from flask_session import Session


SESSION_TYPE = 'filesystem'
app = Flask(__name__)
app.config.from_object(__name__)

Session(app)
Session(app)

# database
users = [
    {
        "id": 1,
        "username": "test",
        "password": "test",
        "balance": 2000,
    },
    {
        "id": 2,
        "username": "hacker",
        "password": "hacker",
        "balance": 0,
    }
]


k_auth = "authorized"
k_login = "login"
k_last_changed = 'last'
k_token = 'token'

symbols = 'rth34rwereffret4353uhradg3g43tygyf32tt67wefgs'

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        for candidate in users:
            if candidate.get('username') == username and candidate.get('password') == password:
                session[k_auth] = True
                session[k_login] = username
                return redirect(url_for('accounts'))
    else:
        if session.get(k_auth):
            return redirect(url_for('accounts'))
        return render_template("login.html")

def generate():
    token = list(symbols)
    np.random.shuffle(token)
    session[k_token] = ''.join(token)
    session[k_last_changed] = datetime.datetime.now()

def update_csrf_token():
    if not session.get(k_token):
        generate()
    else:
        if (datetime.datetime.now() - session[k_last_changed]).total_seconds() > 40:
            generate()

@app.route("/accounts", methods=["GET", "POST"])
def accounts():
    if not session.get(k_auth):
        return redirect(url_for('login'))

    user = users[0]

    update_csrf_token()

    if request.method == "POST":
        if session.get(k_token) != request.form.get('csrf_token'):
            return redirect(url_for('accounts'))

        amount = int(request.form.get("amount"))
        account = int(request.form.get("account"))

        transfer_to = users[1]

        if amount <= user["balance"] and transfer_to:
            user["balance"] -= amount
            transfer_to["balance"] += amount

        return redirect(url_for('accounts'))

    return render_template("accounts.html",
                           balance=user["balance"],
                           username=user["username"],
                           csrf_token=session.get(k_token)
    )


if __name__ == "__main__":
    app.run(host='127.0.0.2', port=10000, debug=True)
