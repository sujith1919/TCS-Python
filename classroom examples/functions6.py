#handling variable length keyword - arguments
def add_employee(**kwds):
	print(type(kwds))
	print(kwds)
	
	
	
	
print(add_employee(name="ram",eid=345))
print(add_employee(name="ram"))
print(add_employee(name="ram",eid=345,email="ram@abc.com"))