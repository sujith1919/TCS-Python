#handling variable length arguments
def add(*args):
	print(type(args))
	print(args)
	return sum(args)
	
	
print(add(2,3))
print(add(2,3,4))
print(add(2,3,4,6,8,9,0,5,6,7))