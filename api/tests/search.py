import requests
import json

url = 'https://seedbox.tk/api/Users'
headers = {'Content-Type': 'application/json'}

filters = [dict(fname='Test')]
params = dict(q=json.dumps(dict(filters=filters)))
print params

response = requests.get(url, params=params, headers=headers)
print(response.json())
