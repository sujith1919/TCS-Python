import urllib.request as web
urls=[
"http://www.google.com",
"http://www.mongofactory.com",
"http://www.indianblooddonors.com",
"http://www.fghukmnbfthnmlkjhbvcfgb.com"
]

while True:
	for url in urls:
		try:
			txt=web.urlopen(url).read()
			print ("The site {} is up".format(url))
		except web.URLError:
			print ("The site {} is down".format(url))
