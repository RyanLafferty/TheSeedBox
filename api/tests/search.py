import requests
import json

url = 'https://seedbox.tk/api/Users'
headers = {'Content-Type': 'application/json'}

filters = [dict(name='fname', op='like', val='Test')]
params = dict(q=json.dumps(dict(filters=filters)))

response = requests.get(url, params=params, headers=headers)
assert response.status_code == 200
print(response.json())
