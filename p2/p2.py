import requests
access_token = 'gho_454rgrtg54ldzDLjzFS7kvmN5Ki1mNXFK'
headers = {"Authorization": f"token {access_token}"}
endpoint = "https://api.github.com/applications/8d2343254wrw1982160ee52/grant"
response = requests.delete(endpoint, headers=headers)

data = response.json()
print(data)