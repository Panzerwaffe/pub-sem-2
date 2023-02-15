from flask import Flask, request, redirect
from utils import *

app = Flask(__name__)

@app.route("/authorization")
def auth():
    code = request.args.get("code")
    token = get_token_by_code(code)
    name, username, privates = get_user_info(token)
    return f"<h1> вы {name} авторизованы и у вас {privates} реп :D </h1>"

@app.route("/login")
def login():
    # fast example
    link = generate_link()
    return redirect(link)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=10000)