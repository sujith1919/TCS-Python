import requests
from datetime import datetime

#post to an api

url="http://localhost:8080/addbook"

payload = {'id':7,'bookname':'Hamlet','author':'William Shakespeare'}

r = requests.post(url, data = payload )
if r.ok:
	print("Book added successfully")











