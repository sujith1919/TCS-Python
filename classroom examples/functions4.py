#keyword - arguments
def wish(name,age):
	print("Hello {} you are {} years old".format(name,age))
	
wish("India",70)
wish(70,"India")

wish(age = 70,name = "India")  #keyword-argument style