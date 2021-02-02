import urllib2
urls=[
"http://www.google.com",
"http://www.mongofactory.com",
"http://www.indianblooddonors.com",
"http://www.fghukmnbfthnmlkjhbvcfgb.com"
]

while True:
	for url in urls:
		try:
			txt=urllib2.urlopen(url).read()
			print ("The site {} is up".format(url))
		except urllib2.URLError:
			print ("The site {} is down".format(url))
		