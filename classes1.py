class Employee(object):
	company="Synechron"
	def __init__(self,eid,name,mobile): # constructor
		self.eid=eid
		self.name=name
		self.mobile=mobile
	def getmobile(self):
		print self.mobile
	def setmobile(self,mobile):
		self.mobile=mobile

ramesh=Employee('223','Ramesh Sannareddy','9885970033')
print type(ramesh)
ramesh.getmobile()
ramesh.setmobile('9866309211')
ramesh.getmobile()
print isinstance(ramesh,Employee)









#class with static emp count

class Employee(object):
	company="Cisco"
	__empcount=0
	def __init__(self,id,name,mobile): # constructor
		self.id=id
		self.name=name
		self.mobile=mobile
		Employee.__empcount+=1
	def get_mobile(self):
		print self.mobile
	def set_mobile(self,mobile):
		self.mobile=mobile
	
ramesh=Employee('223','Ramesh Sannareddy','9885970033')#create a new employee
print Employee.__empcount
Employee._empcount=6789
print Employee.__empcount









#class with static method get emp count

class Employee(object):
	company="Cisco"
	_empcount=0
	def __init__(self,id,name,mobile): # constructor
		self.id=id
		self.name=name
		self.mobile=mobile
		Employee._empcount+=1
	def get_emp_count():
		print Employee._empcount
	get_emp_count=staticmethod(get_emp_count)
	def get_mobile(self):
		print self.mobile
	def set_mobile(self,mobile):
		self.mobile=mobile
	def __str__(self):#used when the object is printed
		return str(self.id) + " " + self.name + " " + str(self.mobile)

Employee.get_emp_count()