import requests

import requests

res = requests.post('http://127.0.0.1:10000/api/v1/set_some', data={'q': 1, 'aa': 'bb'})
print(res.text)
print(res.json())


exit()
# do not save like this!!!
app_id = "343rewerfer3452160ee52"
app_secret = "34rrert3rtetgrtg4grg4t"

def generate_link(url_redirect):
    params = dict(client_id=app_id,  # the client ID you received from GitHub when you registered
                  redirect_uri=url_redirect,  # the URL in your application where users will be sent after authorization
                  # scope="",  # type of access
                  response_type="code")  # request the code
    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params=params)
    return response.url

def get_token_by_code(code, url_redirect):
    params = dict(client_id=app_id,
                  client_secret=app_secret,
                  redirect_uri=url_redirect,
                  code=code)

    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, json=params)

    data = response.json()

    token = data.get("access_token")

    return token

def get_user_info(access_token):
    # read the GitHub manual about headers
    headers = {"Authorization": f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers)

    data = response.json()
    username = data.get('login')
    email = data.get('email')

    return username, email
