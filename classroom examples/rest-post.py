import requests
from datetime import datetime

#post to an api

url="http://www.mongofactory.com/apis/postdumppython.php"

payload = {'name':,'loc':,'date':datetime.today()}

r = requests.post(url, data = payload )
if r.ok:
	output=r.text
	print(output)











