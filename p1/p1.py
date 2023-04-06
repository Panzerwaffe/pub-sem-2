import requests

# just to remember

headers = {"fff": "what?"}
endpoint = "https://randomuser.me/api/"

res = requests.get(endpoint, headers=headers)
print(res.json())

req = res.request
print(req)
