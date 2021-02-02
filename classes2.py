#class inheritance

class Employee(object): # base class
	"""this is the base Employee class"""
	code="Emp"
	def __init__(self,id,name,mobile): # constructor
		self.id=id
		self.name=name
		self.mobile=mobile
	def get_mobile(self):
		"""This functions prints the mobile#"""
		print self.mobile
	def get_salary(self,days):
		return 1000*days
	def set_mobile(self,mobile):
		self.mobile=mobile
	def __str__(self):#used when the object is printed
		return Employee.code + ":" + str(self.id) + " " + self.name + " " + str(self.mobile)

		
class Trainee(Employee):#derived class
	code="Trainee"
	


ramesh=Trainee('223','Ramesh Sannareddy','9885970033')#create a new Trainee
ramesh.get_mobile()
ramesh.set_mobile('9440924316')
ramesh.get_mobile()
print type(ramesh)




