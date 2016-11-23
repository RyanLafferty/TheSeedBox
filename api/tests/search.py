import requests
import json

url = 'https://seedbox.tk/api/Retailers'
headers = {'Content-Type': 'application/json'}

#filters = [dict(name='fname', op='like', val='Test')]
#params = dict(q=json.dumps(dict(filters=filters)))
params = (json.dumps(dict(id=3, name='Walmart', url='www.walmart.ca')))
print params

response = requests.post(url, params=params, headers=headers)
#assert response.status_code == 200
print(response.json())
