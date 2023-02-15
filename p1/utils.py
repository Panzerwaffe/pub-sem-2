import requests

# do not save like this!!!
app_id = "ваш client id"
app_secret = "ваш client secret"
url_redirect = "http://127.0.0.1:10000/authorization"


def generate_link():
    params = dict(client_id=app_id,  # the client ID you received from GitHub when you registered
                  redirect_uri=url_redirect,  # the URL in your application where users will be sent after authorization
                  scope="user",  # type of access
                  response_type="code")  # request the code
    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params=params)

    return response.url

def get_token_by_code(code):
    params = dict(client_id=app_id,
                  client_secret=app_secret,
                  redirect_uri=url_redirect,
                  code=code)
    headers = {"Accept": "application/json"}
    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, params=params, headers=headers)

    data = response.json()
    token = data.get("access_token")

    return token

def get_user_info(access_token):
    # read the GitHub manual about headers
    headers = {"Authorization": f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers)

    data = response.json()
    name = data.get("name")
    username = data.get("login")
    private_repos_count = data.get("total_private_repos")

    return name, username, private_repos_count
