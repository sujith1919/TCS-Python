import requests
from datetime import datetime

#post to an api

url="http://www.mongofactory.com/apis/postdumppython.php"

payload = {'name':'ramesh','loc':'hyderabad','date':datetime.today()}

r = requests.post(url, data = payload )
if r.ok:
	output=r.text
	print(output)


















url = 'https://api.abc.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))

#put

r = requests.put('http://abc.org/put', data = {'key':'value'})

#delete
r = requests.delete('http://abc.org/delete')
