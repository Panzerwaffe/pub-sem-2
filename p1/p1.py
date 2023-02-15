import requests

# just to remember

headers = {"fff": "what?"}
endpoint = "https://randomuser.me/api/"

res = requests.get(endpoint, headers=headers)
print(res)

req = res.request
print(req)
