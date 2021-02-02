#simplest class

class Car(object): #by convention all class names start with capital letter
	pass
	
#class with one method

class Car(object):
	def fuel(self):
		print "Water"

zen=Car()#instantiate a new Car
zen.fuel()

#class with one method and one class variable

class Car(object):
	Emission_Norm="Bharath III"
	def fuel(self):
		print "Water"

print Car.Emission_Norm
Car.fuel()#This will give an error
zen=Car()#instantiate a new Car
zen.fuel()
print zen.Emission_Norm