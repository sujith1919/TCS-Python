#global keyword
age = 16
def grow():
	global age
	print(age)
	age+=1
	print(age)
grow()
