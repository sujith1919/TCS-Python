#function with default values

def circlearea(radius,pi=3.14285):
	return pi * radius * radius
	
print(circlearea(45,3.14))
print(circlearea(34))

#variable scope

global_var = 45
a=450
def abc():
	local_var = 25
	a=254
	print(local_var,a,global_var)
abc()
#print(local_var,a,global_var)
print(a,global_var)
