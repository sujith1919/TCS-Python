#passing functions

a=["kulu","manali","leh","ooty","araku"]

b = sorted(a)
print(b)

print(sorted(a,reverse=True))
print(sorted(a,reverse=True,key=len))

def counta(x):
	"""this counts the number of 'a's in a string"""
	return x.count('a')
	
print(sorted(a,key=counta))
